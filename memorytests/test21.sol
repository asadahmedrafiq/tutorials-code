// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test21.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test21 {
   
    constructor() {
    }
// assign6 is an implementation of aliasing using two-dimensional fixed sized array.
// assign6 accepts two dimensional fixed sized arrays , their respective indices and value.
// The test invovlves the pointer-to-pointe assignment followed by the value-to-pointer assignemnt.

  function t21(uint8[20][20] memory x6, uint8 i6, uint8 j6, uint8 value6) 
    public 
    returns (uint8[20][20] memory)  
    {
        x6[i6][j6] = value6;
      return x6;
    }

}