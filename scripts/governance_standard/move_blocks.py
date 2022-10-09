#Code to 'move' blocks forward 
#Since its a virtual system, blocks dont move unless you move it yourself

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

def move_blocks(amount):
    for block in range(amount):
        get_account().transfer(get_account(), "0 ether")
    print(chain.height)

def main():
    #To artificially move the blockchain forward
    BLOCKS_TO_MOVE = int(input("Enter the number of blocks to move forward by: "))

    move_blocks(BLOCKS_TO_MOVE)
    print(f"Moved by {BLOCKS_TO_MOVE}")

    