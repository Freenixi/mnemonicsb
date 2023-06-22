# mnemonicsb
 This Python script generates mnemonic phrases, derives Ethereum addresses, and checks their balance using etherscan.io API. It saves results in a text file and SQLite database, offering independent address generation without 3rd-party reliance, facilitating quick creation of multiple addresses with 12-word phrases and private keys.

====================================
=============README=================
====================================
# Mnemonic Phrase Address Checker "ala Reverse Mining" - (mnemonicsb.py)
====================================

This Python script generates mnemonic phrases, derives Ethereum addresses from them, and checks the balance of those addresses using the etherscan.io API. The script also saves the results in a SQLite database.

Dependencies:
- mnemonic: Python library for generating mnemonics
- eth-utils: Python utility library for Ethereum-related functionality
- eth-account: Python library for working with Ethereum accounts
- requests: Python library for making HTTP requests
- xml.etree.ElementTree: Python standard library for parsing XML

Configuration:
The script requires a configuration file named "mnemonicsb.config" in the same directory. The configuration file specifies the wordlist, Etherscan API key, and various settings for statistics and seed phrases. Modify the configuration file to suit your needs.

Configuration Settings:
1. wordlist:
   - <path>: Path to a local wordlist file (e.g., <path>example.txt</path>).
   - <url>: URL of a wordlist file hosted online (e.g., <url>https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt</url>).
   - Note: Choose either <path> or <url>. Only one option can be used at a time.

2. apietherscanio:
   - <api>: Your Etherscan API key. Replace the example key with your own.
   - Note: By default, the script is set to use the free plan limit of 5 requests per second. If you have a paid plan, you can adjust this value in the Python script accordingly.

3. statistics:
   - <totalchecked>: Save statistics about the total number of addresses checked (true/false).
   - <bip39fail>: Save invalid BIP-39 mnemonics to a separate database (true/false).

4. seedphrase:
   - <skiplist>: Skip checking previously generated addresses (true/false).

Usage:
- Users can utilize this script to generate a specific number of Ethereum addresses independently from any third-party services. This allows for enhanced security and privacy, as the generation process is performed locally and does not rely on external sources.
- The script provides flexibility in terms of wordlist selection. You can either specify a local wordlist file or provide a URL to an online wordlist file. Choose the option that suits your requirements.

Future Potential / Roadmap:
- Separate Python Script for Address Double-Checking: As part of the roadmap, a separate Python script could be developed specifically for address double-checking. This script would periodically recheck the previously checked addresses to ensure their status remains consistent. This double-checking process would contribute to the accuracy and reliability of the generated results.

- Checking More Addresses: In future updates, the script can be enhanced to check multiple addresses derived from the same mnemonic phrase. This would involve iterating through different derivation paths or using additional indices to generate and check a larger set of addresses. By expanding the address checking scope, the script can uncover a wider range of balances associated with a single mnemonic phrase.

- Direct Blockchain Interaction: Instead of relying on the etherscan.io API, future updates could include the ability to directly interact with a locally downloaded Ethereum blockchain. This would allow for faster address checking and eliminate the reliance on external APIs.

- Synchronization via Torrent Technology: To enhance address checking efficiency and distribute the workload, future updates could introduce the use of torrent technology for synchronizing the results of address checking across multiple users. This would enable users to collaborate and share the progress of address checking, reducing duplication of effort and improving overall efficiency.

- Support for Multiple Chains/Networks: Currently, the script focuses on Ethereum addresses derived from mnemonic phrases. However, future updates can introduce support for additional blockchain networks and their respective address formats. This would allow users to check the balances of addresses on various chains, such as Bitcoin, Litecoin, or other compatible networks. The inclusion of multiple chains/networks expands the script's utility and provides a broader perspective on address balances.

- Quantum Computing Efficiency: Looking ahead, the emergence of quantum computers may significantly impact the efficiency of the "Reverse Mining" concept. Quantum computers have the potential to solve certain complex computational problems, such as factoring large numbers, more efficiently than classical computers. In the context of address checking, the utilization of quantum algorithms could expedite the process of identifying empty addresses and improve overall efficiency. Exploring the integration of quantum computing techniques into the script's functionality may be considered in future updates.

Notes:
- This script provides a convenient way to generate mnemonic phrases, derive Ethereum addresses, and check their balances.
- Mnemonic phrases are generated either using a specified wordlist file or directly from the script itself.
- The script can be used independently to generate 12-word phrases and their corresponding addresses without relying on browsers or any 3rd party sources/sides.
- It offers flexibility in choosing the wordlist source by allowing users to specify a local file path or a URL for downloading the wordlist.
- The use of the Etherscan API allows for quick and easy balance checks of Ethereum addresses.
- The configuration file provides customizable options for adjusting various settings of the script.
- Users are encouraged to review and modify the configuration file to suit their specific needs.
- It is important to exercise caution and ensure the security of the generated mnemonic phrases and derived addresses.
- The script can be expanded to support additional chains/networks and check more addresses under the same mnemonic phrase in future updates.
- As quantum computing advances, the efficiency of "Reverse Mining" may be enhanced, and exploring its integration into the script's functionality could be considered in the future.
- These roadmap items outline potential future developments and are subject to implementation feasibility, technological advancements, and project goals.
- Regular updates and improvements to the script may be made based on user feedback, community contributions, emerging technologies, and advancements in quantum computing research.
- Reverse Mining Concept: While it may seem like a unique and unconventional idea, the project could explore the concept of reverse mining, wherein the objective is to identify empty addresses rather than mining blocks. By leveraging mnemonic phrases and their derived addresses, the script aims to efficiently identify empty addresses in the Ethereum network.
- Generating random mnemonic phrases does not guarantee access to real accounts or funds.
- Use caution and do not share the generated mnemonics or derived addresses with others.
- This script is for educational and testing purposes only.

Please note that the security and privacy of the generated mnemonic phrases and derived addresses are the responsibility of the users. Exercise caution when handling and storing sensitive information.

==================================================
===================README=========================
==================================================
# EXTRA - Mnemonics to Private Key Conversion - (bconverter.py, mnemonics2pkey.py)
==================================================

bconverter.py - reads the contents of a file named "valid.mnemonicsb.txt" and extracts mnemonics from each line for the mnemonics2pkey.py
mnemonics2pkey.py allows you to convert mnemonic phrases into their corresponding private keys and wallet addresses for cryptocurrency wallets. The generated private keys can be used to access the respective wallets without the need to rely on external services.

--------------------------------------------------
Usage
--------------------------------------------------

1. Install Dependencies:
   - Ensure you have Python 3.x installed on your system.
   - Install the necessary libraries by running the following command:
       ```
       pip install eth-account
       ```

2. Prepare Mnemonic Phrases:
   - Create a file named `mnemonics.txt`.
   - Add each mnemonic phrase on a new line in the file. One phrase per line.

3. Run the Script:
   - Execute the script by running the following command:
       ```
       python mnemonics2pkey.py
       ```

4. Output:
   - The script will generate a file named `apkey.txt` in the same directory.
   - The `apkey.txt` file will contain the corresponding mnemonic phrases, private keys, and wallet addresses.

--------------------------------------------------
Important Note
--------------------------------------------------

- Exercise caution when handling mnemonic phrases and private keys.
- Keep the `mnemonics.txt` and `apkey.txt` files secure as they contain sensitive information.

--------------------------------------------------
Dependencies
--------------------------------------------------

- eth-account: A library for working with Ethereum accounts and private keys.

--------------------------------------------------
Disclaimer
--------------------------------------------------

- This script is provided for educational purposes only.
- Use it responsibly and at your own risk.
- The creators and contributors of this script are not responsible for any misuse or unauthorized access to wallets.


==================================================
===================README=========================
==================================================
# Recommended versions for dependencies:
==================================================
bip32utils==0.3.post4
eth-account==0.9.0
requests==2.27.1
mnemonic==0.19
requests==2.27.1
