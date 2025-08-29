// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test26.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test26 {
   
    constructor() {
    }


function t26(uint8[]memory x31, uint8 i31, uint8 j31, uint8 value31, uint8[] memory y31) 
    public 
    returns (uint8[] memory)  
    {
      x31[i31] = y31[j31];
      y31[j31]= value31;
      return x31;
    }
}