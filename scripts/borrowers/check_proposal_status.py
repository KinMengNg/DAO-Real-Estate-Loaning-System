from ..governance_standard.deploy_and_run import PROPOSAL_DESCRIPTION
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account

#Brownie interacts with the solidity files
from brownie import (
    GovernorContract,
    GovernanceToken,
    GovernanceTimeLock,
    ValuePool,
    Contract,
    config,
    network,
    accounts,
    chain,
)
from web3 import Web3, constants
import time

def check_status(proposal_id):
    # States: {Pending, Active, Canceled, Defeated, Succeeded, Queued, Expired, Executed }
    return GovernorContract[-1].state(proposal_id)

def main():
    ##Mock up to show how borrowers will interact with the system
    PROPOSAL_ID = int(input("Enter Proposal ID: "))

    print(f" This proposal is currently {check_status(PROPOSAL_ID)}")