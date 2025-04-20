import time
from datetime import datetime
from web3 import Web3

# Define supported chains and their RPC URLs
chains = {
    'ethereum': {'rpc': 'https://ethereum-rpc.publicnode.com', 'chain_id': 1},
    'arbitrum': {'rpc': 'https://arb1.arbitrum.io/rpc', 'chain_id': 42161},
    'optimism': {'rpc': 'https://mainnet.optimism.io', 'chain_id': 10},
    'base': {'rpc': 'https://mainnet.base.org', 'chain_id': 8453},
    'bsc': {'rpc': 'https://bsc-dataseed1.binance.org/', 'chain_id': 56},
    'polygon': {'rpc': 'https://polygon-rpc.com/', 'chain_id': 137},
    'fantom': {'rpc': 'https://rpcapi.fantom.network', 'chain_id': 250},
    'gravity': {'rpc': 'https://rpc.gravity.xyz', 'chain_id': 1625},
    'sonic': {'rpc': 'https://sonic.api.onfinality.io/public', 'chain_id': 146},
    'Soneium': {'rpc': 'https://soneium.drpc.org', 'chain_id': 1868},
    'Zora': {'rpc': 'https://rpc.zora.energy', 'chain_id': 7777777}
  # Add more...
}

# Define example wallets to scan and rescue
wallets = [
    {
        'private_key': 'YOUR_PRIVATE_KEY_1',
        'from_address': Web3.to_checksum_address('0xYourFromAddress1'),
        'safe_address': Web3.to_checksum_address('0xYourSafeAddress1')
    },
    {
        'private_key': 'YOUR_PRIVATE_KEY_2',
        'from_address': Web3.to_checksum_address('0xYourFromAddress2'),
        'safe_address': Web3.to_checksum_address('0xYourSafeAddress2')
    }
  # Add More
]

# Logging function
def log(msg):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now().isoformat()} | {msg}\n")
    print(msg)

# Scan all wallets and rescue gas to safe addresses
def scan_all_wallets():
    for wallet in wallets:
        for name, chain in chains.items():
            try:
                w3 = Web3(Web3.HTTPProvider(chain['rpc']))
                if not w3.is_connected():
                    log(f"[{name.upper()}] RPC FAILED.")
                    continue

                balance = w3.eth.get_balance(wallet['from_address'])
                eth_balance = w3.from_wei(balance, 'ether')
                log(f"[{name.upper()}] [{wallet['from_address']}] Balance: {eth_balance:.18f}")

                if balance == 0:
                    continue

                nonce = w3.eth.get_transaction_count(wallet['from_address'])
                network_gas_price = w3.eth.gas_price
                max_gas_price = w3.to_wei('50', 'gwei')
                gas_price = min(network_gas_price, max_gas_price)
                gas_limit = 21000
                fee = gas_price * gas_limit

                if balance <= fee:
                    log(f"[{name.upper()}] Not enough to cover gas fee.")
                    continue

                # Add buffer to avoid underestimation errors
                buffer = int(fee * 0.01)
                transferable_value = balance - fee - buffer

                if transferable_value <= 0:
                    log(f"[{name.upper()}] Transferable value too small after buffer.")
                    continue

                tx = {
                    'nonce': nonce,
                    'to': wallet['safe_address'],
                    'value': transferable_value,
                    'gas': gas_limit,
                    'gasPrice': gas_price,
                    'chainId': chain['chain_id']
                }

                signed_tx = w3.eth.account.sign_transaction(tx, wallet['private_key'])
                tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
                log(f"[{name.upper()}] TX SENT for {wallet['from_address']} -> {tx_hash.hex()}")

            except Exception as e:
                log(f"[{name.upper()}] [{wallet['from_address']}] Error: {str(e)}")

# Loop every 30 seconds
while True:
    scan_all_wallets()
    time.sleep(30)
