// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test28.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test28 {
   
    constructor() {
    }


function t28(uint8[20]memory x31, uint8 i31, uint8 j31, uint8 k31, uint8 value31, uint8[20] memory y31, uint8[20] memory z31) 
    public 
    returns (uint8[20] memory)  
    {
      x31[i31] = z31[j31];
      z31[j31]= y31[k31];
      y31[k31] = value31;
      return x31;
    }
}