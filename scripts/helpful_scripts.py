from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000

# add to brownie-config.yaml
"""
dotenv: .env
wallets:
  from_key: ${PRIVATE_KEY}
"""
# and in the .env file
"""
export PRIVATE_KEY=0x
export WEB3_INFURA_PROJECT_ID=7442337d8a644907bafcdff58b1a0a12
"""


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deplowing Mocks....")
    if len(MockV3Aggregator) <= 0:  # its an array containing all the contracts deployed
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks deployed")
