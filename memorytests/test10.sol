// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test10.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test10 {
   
    constructor() {
    }
// assign2dp2p2 is an implementation of aliasing using two-dimensional fixed sized array.
// assign6 accepts two dimensional fixed sized arrays , their respective indices and value.
// The test invovlves the pointer-to-pointe assignment followed by the value-to-pointer assignemnt.

  function assign2dp2p2(uint8[10][10] memory x6, uint8 i6, uint8 j6, uint8 k6, uint8 value6, uint8[10][10] memory y6) 
    public 
    returns (uint8[10][10] memory)  
    {
      x6[i6] = y6[j6];
      y6[j6][k6] = value6;
      return x6;
    }

}