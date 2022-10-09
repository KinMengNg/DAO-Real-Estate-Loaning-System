from errno import EHOSTUNREACH
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account

#Brownie interacts with the solidity files
from brownie import (
    GovernorContract,
    GovernanceToken,
    GovernanceTimeLock,
    Treasury,
    Contract,
    config,
    network,
    accounts,
    chain,
)
from web3 import Web3, constants
import time

def transfer(amount, account, account_to_receive):
    token = GovernanceToken.deploy({'from': account})
    token.transfer(account_to_receive, amount, {'from': account})

def mint_and_give(amount, account_to_give, treasury):
    #mint the token by the amount
    token = GovernanceToken.deploy("MICASA", "MCS", amount, {'from': treasury})

    token.transfer(account_to_give, amount, {'from': treasury})
    

def main():
    ACCOUNT = get_account()

    TREASURY = Treasury.address

    #In gwei
    DEPOSIT_AMOUNT = int(input("Enter Deposit Amount [In Gwei]: "))

    #For now, we do a one-to-one convertion with our MICASA token
    
    #Transfer Gwei to Treasury
    transfer(DEPOSIT_AMOUNT, ACCOUNT, TREASURY)

    #Give MICASA token to account
    mint_and_give(DEPOSIT_AMOUNT, ACCOUNT, TREASURY)
    print(f"received {DEPOSIT_AMOUNT} MICASA")







    
