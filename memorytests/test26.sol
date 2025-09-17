// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test26.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test26 {
   
    constructor() {
    }


function t26(uint8[] memory x, uint8 i, uint8 j, uint8 value, uint8[] memory y) 
    pure
    public 
    returns (uint8[] memory)  
    {
      x [i] = y [j];
      y [j] = value;
      return x;
    }
}