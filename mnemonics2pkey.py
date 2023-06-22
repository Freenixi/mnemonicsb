from eth_account import Account

# Enable unaudited HD wallet features
Account.enable_unaudited_hdwallet_features()

# Define the path to the mnemonics file
mnemonics_file = "mnemonics.txt"
output_file = "apkey.txt"

# Read the mnemonic phrases from the file
with open(mnemonics_file, "r") as file:
    mnemonic_phrases = [line.strip() for line in file]

# Derive the private keys, addresses, and save to the file
with open(output_file, "w") as file:
    for phrase in mnemonic_phrases:
        # Derive the private key from the mnemonic
        private_key_bytes = Account.from_mnemonic(phrase)._private_key
        private_key_hex = private_key_bytes.hex()

        # Derive the wallet address from the private key
        account = Account.from_key(private_key_hex)
        wallet_address = account.address

        # Write the details to the file
        file.write("Mnemonic: {}\n".format(phrase))
        file.write("Private Key: {}\n".format(private_key_hex))
        file.write("Wallet Address: {}\n".format(wallet_address))
        file.write("-" * 50 + "\n")

print("Private keys and addresses saved to {}.".format(output_file))

