// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test27.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test27 {
   
    constructor() {
    }


function t27(uint8[5]memory x31, uint8 i31, uint8 j31, uint8 k31, uint8 value31, uint8[5] memory y31, uint8[5] memory z31) 
    public 
    returns (uint8[5] memory)  
    {
      x31[i31] = z31[j31];
      z31[j31]= y31[k31];
      return x31;
    }
}