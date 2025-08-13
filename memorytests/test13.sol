
    // SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test13.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test13 {
   
    constructor() {
    }
// assigndyvtp is a function that accepts a dynamic memory array, performs an value-to-pointer assignment  operations and rerutrns 
 // the dynamic array. 
 // The function is design to test Certora verification of dynamic arrays

 function assigndyvp(uint8[] memory x7, uint8 i7, uint8 y7) 
    public 
    returns (uint8[] memory)  
    {
      x7[i7] = y7;
      return x7;
    }
}