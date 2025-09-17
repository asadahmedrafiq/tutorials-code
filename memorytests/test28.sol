// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test28.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test28 {
   
    constructor() {
    }


function t28(uint8[20]memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[20] memory y, uint8[20] memory z) 
    pure
    public 
    returns (uint8[20] memory)  
    {
      x [i] = z [j];
      z [j]= y [k];
      y [k] = value;
      return x;
    }
}