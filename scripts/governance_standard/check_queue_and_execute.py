#Check if the the proposal has passed deadline and check outcome, if approved, queue and execute
#This script should be done periodically on every active proposal ID
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

def check_outcome(proposal_id):
    # States: {Pending, Active, Canceled, Defeated, Succeeded, Queued, Expired, Executed }
    outcome = GovernorContract[-1].state(proposal_id)
    return outcome


#Execute in 
def queue_and_execute(loan_amount, down_payment_amount, interest_rate, tenure, proposal_description):
    account = get_account()
    # time.sleep(VOTING_PERIOD + 1)
    # we need to explicity give it everything, including the description hash
    # it gets the proposal id like so:
    # uint256 proposalId = hashProposal(targets, values, calldatas, descriptionHash);
    # It's nearlly exactly the same as the `propose` function, but we hash the description
    args = (loan_amount, down_payment_amount, interest_rate, tenure, proposal_description)
    encoded_function = Contract.from_abi("Treasury", Treasury[-1], Treasury.abi).store.encode_input(
        *args
    )
    # this is the same as ethers.utils.id(description)
    description_hash = Web3.keccak(text=proposal_description).hex()
    tx = GovernorContract[-1].queue(
        [Treasury[-1].address],
        [0],
        [encoded_function],
        description_hash,
        {"from": account},
    )
    tx.wait(1)

    if network.show_active() == 'development':
        time.sleep(1)

    tx = GovernorContract[-1].execute(
        [Treasury[-1].address],
        [0],
        [encoded_function],
        description_hash,
        {"from": account},
    )
    tx.wait(1)
    print(Treasury[-1].retrieve())

def main():
    PROPOSAL_ID = int(input("Enter Proposal ID to Check Outcome"))
    outcome = check_outcome(PROPOSAL_ID)

    if outcome == "Succeeded":
        #Mock up to show how approved proposals will be queued and executed
        PROPOSAL_DESCRIPTION, LOAN_AMOUNT, DOWN_PAYMENT_AMOUNT, INTEREST_RATE, TENURE = GovernorContract[-1].decode_input(PROPOSAL_ID)
        queue_and_execute(PROPOSAL_DESCRIPTION, LOAN_AMOUNT, DOWN_PAYMENT_AMOUNT, INTEREST_RATE, TENURE)

        







