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

# Governor Contract
QUORUM_PERCENTAGE = 30
# VOTING_PERIOD = 45818  # 1 week - more traditional.
# You might have different periods for different kinds of proposals
VOTING_PERIOD = 5  # 5 blocks
VOTING_DELAY = 1  # 1 block

# Timelock
# MIN_DELAY = 3600  # 1 hour - more traditional
MIN_DELAY = 1  # 1 seconds

# Proposal
PROPOSAL_DESCRIPTION = "Proposal #1: Store 1 in the Box!"
NEW_STORE_VALUE = 5


def deploy_governor():
    account = get_account()
    governance_token = (
        GovernanceToken.deploy(
            {"from": account},
            publish_source=config["networks"][network.show_active()].get(
                "verify", False
            ),
        )
        if len(GovernanceToken) <= 0
        else GovernanceToken[-1]
    )
    governance_token.delegate(account, {"from": account})
    print(f"Checkpoints: {governance_token.numCheckpoints(account)}")
    governance_time_lock = governance_time_lock = (
        GovernanceTimeLock.deploy(
            MIN_DELAY,
            [],
            [],
            {"from": account},
            publish_source=config["networks"][network.show_active()].get(
                "verify", False
            ),
        )
        if len(GovernanceTimeLock) <= 0
        else GovernanceTimeLock[-1]
    )
    governor = GovernorContract.deploy(
        governance_token.address,
        governance_time_lock.address,
        QUORUM_PERCENTAGE,
        VOTING_PERIOD,
        VOTING_DELAY,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    # Now, we set the roles...
    # Multicall would be great here ;)
    proposer_role = governance_time_lock.PROPOSER_ROLE()
    executor_role = governance_time_lock.EXECUTOR_ROLE()
    timelock_admin_role = governance_time_lock.TIMELOCK_ADMIN_ROLE()
    governance_time_lock.grantRole(proposer_role, governor, {"from": account})
    governance_time_lock.grantRole(
        executor_role, constants.ADDRESS_ZERO, {"from": account}
    )
    tx = governance_time_lock.revokeRole(
        timelock_admin_role, account, {"from": account}
    )
    tx.wait(1)
    # Guess what? Now you can't do anything!
    # governance_time_lock.grantRole(timelock_admin_role, account, {"from": account})


def deploy_treasury():
    account = get_account()
    treasury = Treasury.deploy({"from": account})
    tx = treasury.transferOwnership(GovernanceTimeLock[-1], {"from": account})
    tx.wait(1)


def main():
    deploy_governor()
    deploy_treasury()

