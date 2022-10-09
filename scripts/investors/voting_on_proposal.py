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

def vote(proposal_id: int, vote: int, reason):
    # 0 = Against, 1 = For, 2 = Abstain for this example
    # you can all the #COUNTING_MODE() function to see how to vote otherwise
    stance = ''
    if vote == 0:
        stance = "Against"
    elif vote == 1:
        stance = 'For'
    elif vote == 2:
        stance = "Abstain"
    
    print(f"voting {stance} on {proposal_id}")
    account = get_account()
    tx = GovernorContract[-1].castVoteWithReason(
        proposal_id, vote, reason, {"from": account}
    )
    tx.wait(1)
    print(tx.events["VoteCast"])

def main():
    #Mock up to show how borrowers will interact with the system
    PROPOSAL_ID = int(input("Enter Proposal ID to Vote On: "))
    VOTE = int(input("Enter your vote [0 = Against, 1 = For, 2 = Abstain]: "))
    REASON = input("Enter Reason: ")

    vote(PROPOSAL_ID, VOTE, REASON)


