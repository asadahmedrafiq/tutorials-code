
    // SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test15.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memory variables in Solidity
 */
contract test15 {
   
    constructor() {
    }

 function t15(uint8[50][50] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[50][50] memory y) 
    pure
    public 
    returns (uint8[50][50] memory)  
    {
      x [i] = y [j];
      y [j][k] = value;
      return x;
    }
}
