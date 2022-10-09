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

def main():
    #Mock up on how investors can view proposals.
    #Actual thing should be able to view all proposals at a time through an app/website
    PROPOSAL_ID = int(input("Enter Proposal ID to View"))

    PROPOSAL_DESCRIPTION, LOAN_AMOUNT, DOWN_PAYMENT_AMOUNT, INTEREST_RATE, TENURE = GovernorContract[-1].decode_input(PROPOSAL_ID)
    
    print(f"""
    Proposal Description:
    {PROPOSAL_DESCRIPTION}
    """)
    print(f"Loan Amount: {LOAN_AMOUNT}")
    print(f"Down Payment Amount: {DOWN_PAYMENT_AMOUNT}")
    print(f"Interest Rate: {INTEREST_RATE}")
    print(f"Tenure: {TENURE}")
