from web3 import Web3


INFURA_URL = 'https://mainnet.infura.io/v3/c6da68355e194ff1a456df7951293b25'

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
# block_number = web3.eth.block_number
account = "0xB96F9AaA9e0873e42b6Ee35E1cf26C337fE4120a"
balance = web3.eth.get_balance(account) /  10 ** 18
print(balance)
