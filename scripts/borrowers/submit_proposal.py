from ..governance_standard.deploy_and_run import PROPOSAL_DESCRIPTION
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

def propose(loan_amount, down_payment_amount, interest_rate, tenure, proposal_description):
    account = get_account()
    # With more args, just add commas and the items
    # This is a tuple
    # If no arguments, use `eth_utils.to_bytes(hexstr="0x")`
    args = (loan_amount, down_payment_amount, interest_rate, tenure)
    # We could do this next line with just the Contract object
    # But this is to show it can be any function with any contract
    # With any arguments
    encoded_function = Contract.from_abi("ValuePool", Treasury[-1], Treasury.abi).store.encode_input(
        *args
    )
    print(encoded_function)
    propose_tx = GovernorContract[-1].propose(
        [Treasury[-1].address],
        [0],
        [encoded_function],
        proposal_description,
        {"from": account},
    )
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        tx = account.transfer(accounts[0], "0 ether")
        tx.wait(1)
    propose_tx.wait(2)  # We wait 2 blocks to include the voting delay
    # This will return the proposal ID, brownie.exceptions.EventLookupError will be 
    # thrown if ProposalCreated event is not emitted.
    proposal_id = propose_tx.events['ProposalCreated']['proposalId'] # you could also do `propose_tx.return_value` if your node allows
    print(f"Proposal state {GovernorContract[-1].state(proposal_id)}")
    print(
        f"Proposal snapshot {GovernorContract[-1].proposalSnapshot(proposal_id)}"
    )
    print(
        f"Proposal deadline {GovernorContract[-1].proposalDeadline(proposal_id)}"
    )
    return proposal_id


def main():
    #Mock up to show how borrowers will interact with the system
    PROPOSAL_DESCRIPTION = input("Enter Proposal description: ")
    LOAN_AMOUNT = int(input("Enter Loan Amount: "))
    DOWN_PAYMENT_AMOUNT = int(input("Enter Down Payment Amount: "))
    INTEREST_RATE = float(input("Enter Interest Rate: "))
    TENURE = int(input("Enter Length of Tenure: "))

    proposal_id = propose(LOAN_AMOUNT, DOWN_PAYMENT_AMOUNT, INTEREST_RATE, TENURE, PROPOSAL_DESCRIPTION)
    print(f"Proposal ID: {proposal_id}")






    
