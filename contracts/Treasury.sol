// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/access/Ownable.sol";

//Controls the total value of the DAO pool
//onlyOwner is inheritted from Ownable, the owner will be the TimeLock contract
contract Treasury is Ownable {
    uint256 private totalValue;

    // Emitted when the stored value changes
    event ValueChanged(uint256 totalValue);

    //Increase the value
    function increase(uint256 newValue) public onlyOwner{
        totalValue = totalValue + newValue;
        emit ValueChanged(totalValue);
    }

    //Decrease the value
    function decrease(uint256 newValue) public onlyOwner{
        totalValue = totalValue - newValue;
        emit ValueChanged(totalValue);
    }

    // Retrieve current pool value
    function retrieve() public view returns (uint256) {
        return totalValue;
    }

    //Receive function so it can receive eth
    receive() external payable {
        emit ForwarderDeposited(msg.sender, msg.value, msg.data);
}
}