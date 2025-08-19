// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test03.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test03 {
   
    constructor() {
    }


function t03(uint8[5]memory x31, uint8 i31, uint8 j31, uint8 value31, uint8[5] memory y31) 
    public 
    returns (uint8[5] memory)  
    {
      x31[i31] = y31[j31];
      y31[j31]= value31;
      return x31;
    }
}