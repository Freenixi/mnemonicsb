import os
import random
import requests
import time
import xml.etree.ElementTree as ET
from mnemonic import Mnemonic
from eth_utils import to_checksum_address, ValidationError
from eth_account import Account
import sqlite3

# Enable experimental Mnemonic feature in eth_account
Account.enable_unaudited_hdwallet_features()

# Parse configuration file
def parse_config():
    tree = ET.parse("mnemonicsb.config")
    root = tree.getroot()

    # Get wordlist settings
    wordlist_elem = root.find("wordlist")
    wordlist_path = wordlist_elem.find("path")
    wordlist_url = wordlist_elem.find("url")
    mnemonic_elem = wordlist_elem.find("mnemonic")
    use_mnemonic_lib = mnemonic_elem is not None and mnemonic_elem.text.lower() == 'true'

    # Get Etherscan API key
    etherscan_api_key = root.find("apietherscanio/api")

    # Get statistics settings
    total_checked_elem = root.find('statistics/totalchecked')
    save_total_checked = total_checked_elem is not None and total_checked_elem.text.lower() == 'true'

    bip39fail_elem = root.find('statistics/bip39fail')
    save_bip39_fail = bip39fail_elem is not None and bip39fail_elem.text.lower() == 'true'

    # Get seedphrase settings
    skiplist_elem = root.find("seedphrase/skiplist")
    skiplist = skiplist_elem is not None and skiplist_elem.text.lower() == 'true'

    return (
        wordlist_path.text if wordlist_path is not None else None,
        wordlist_url.text if wordlist_url is not None else None,
        etherscan_api_key.text if etherscan_api_key is not None else None,
        save_total_checked,
        skiplist,
        save_bip39_fail,
        use_mnemonic_lib,
    )

# Load BIP-39 wordlist
def load_wordlist(wordlist_path, wordlist_url):
    if wordlist_path:
        with open(wordlist_path, 'r') as file:
            words = file.read().strip().split('\n')
    elif wordlist_url:
        response = requests.get(wordlist_url)
        words = response.text.strip().split('\n')
    else:
        raise ValueError("Neither wordlist path nor URL provided in the configuration file.")
    
    return words

# Generate random 12-word mnemonic phrase
def generate_mnemonic_phrase(words, use_mnemonic_lib):
    if use_mnemonic_lib:
        mnemonic = Mnemonic("english")
        return mnemonic.generate(strength=128)
    else:
        return ' '.join(random.choices(words, k=12))

# Derive Ethereum address from mnemonic phrase
def derive_eth_address(phrase):
    try:
        account = Account.from_mnemonic(phrase)
        return account.address
    except ValidationError:
        return None

# Check the balance of the Ethereum address
def check_eth_balance(address, api_key):
    etherscan_url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}'
    response = requests.get(etherscan_url)
    balance = int(response.json()['result']) / 1e18
    return balance

# Main loop
def main():
    try:
        wordlist_path, wordlist_url, etherscan_api_key, save_total_checked, skiplist, save_bip39_fail, use_mnemonic_lib = parse_config()
        words = load_wordlist(wordlist_path, wordlist_url) if not use_mnemonic_lib else None

        # Set up the SQLite database for valid mnemonics
        conn = sqlite3.connect('mnemonics.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS mnemonics (id INTEGER PRIMARY KEY, phrase TEXT, address TEXT, balance REAL)''')
        conn.commit()

        # Set up the SQLite database for invalid mnemonics
        if save_bip39_fail:
            conn_invalid = sqlite3.connect('invalid.mnemonics.db')
            c_invalid = conn_invalid.cursor()
            c_invalid.execute('''CREATE TABLE IF NOT EXISTS invalid_mnemonics (id INTEGER PRIMARY KEY, phrase TEXT)''')
            conn_invalid.commit()

        delay = 1 / 5  # 5 calls per second
        total_checked = 0
        total_with_balance = 0
        invalid_bip39 = 0

        if save_total_checked:
            valid_addresses_file = open("valid.mnemonicsb.txt", "a")

        if skiplist:
            with open("skiplist.txt", "r") as skiplist_file:
                skip_phrases = [line.strip() for line in skiplist_file.readlines()]

        while True:
            phrase = generate_mnemonic_phrase(words, use_mnemonic_lib)

            if skiplist:
                while phrase in skip_phrases:
                    phrase = generate_mnemonic_phrase(words)

            address = derive_eth_address(phrase)

            if address is None:
                invalid_bip39 += 1
                if save_bip39_fail:
                    c_invalid.execute('INSERT INTO invalid_mnemonics (phrase) VALUES (?)', (phrase,))
                    conn_invalid.commit()
                continue

            total_checked += 1
            balance = check_eth_balance(to_checksum_address(address), etherscan_api_key)

            if save_total_checked:
                valid_addresses_file.write(f'"{phrase}":"{address}"\n')

            if balance > 0:
                c.execute('INSERT INTO mnemonics (phrase, address, balance) VALUES (?, ?, ?)', (phrase, address, balance))
                conn.commit()
                total_with_balance += 1
                print(f'Saved mnemonic: {phrase}, address: {address}, balance: {balance}')

            print(f'Statistics: Total checked: {total_checked}, Total with balance: {total_with_balance}, Invalid BIP39: {invalid_bip39}')

            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Stopping the script.")
        conn.close()
        if save_bip39_fail:
            conn_invalid.close()
        if save_total_checked:
            valid_addresses_file.close()

if __name__ == "__main__":
    main()

