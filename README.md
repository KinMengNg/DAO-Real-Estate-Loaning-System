# Project MICASA - DAO-Real-Estate-Loaning-System

## Installation
DAO based off on-chain governance implementation of brownie-mix.

1. python3 -m pip install --user pipx
2. python3 -m pipx ensurepath
3. restart terminal
4. pipx install eth-brownie
5. Install node.js an npm
6. npm install -g yarn
7. yarn add hardhat (DO THIS IN THE LOCAL FOLDER, NOT GLOBALLY)

## How to use

###System Scripts
#### Deployment of contracts (FOR FIRST RUN)
Run "brownie run scripts/governance_standard/deploy_and_run.py --network hardhat"

#### Check Outcome of Loan Proposals and Further Actions
Run "brownie run scripts/governance_standard/check_queue_and_execute.py --network hardhat"

#### Move the blockhain forward (Since on simulating on Virtual Machine)
Run "brownie run scripts/governance_standard/move_blocks.py --network hardhat"

### Borrower Scripts
#### To Submit a Loan Proposal
Run "brownie run scripts/borrowers/submit_proposal.py --network hardhat"

#### To Check Proposal Status
Run "brownie run scripts/borrowers/check_proposal_status.py --network hardhat"

### Investor Scripts
#### Viewing Loan Proposal
Run "brownie run scripts/investors/viewing_proposal.py --network hardhat"


#### Voting on Loan Proposal
Run "brownie run scripts/investors/voting_on_proposal.py --network hardhat"

#### Depositing Ether into the DAO
Run "brownie run scripts/investors/depositing.py --network hardhat"

