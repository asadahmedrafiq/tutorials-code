
    // SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test16.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test16 {
   
    constructor() {
    }

 function t16(uint8[5][5] memory x, uint8 i, uint8 j, uint8 k,  uint8 l, uint8 value, uint8[5][5] memory y, uint8[5][5] memory z) 
    pure
    public 
    returns (uint8[5][5] memory)  
    {
      x[i] = z[j];
      z[j] = y[k];
      y[k][l] = value;
      return x;
    }
}
