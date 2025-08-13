// SPDX-License-Identifier: MIT
// Memory test for value-to-pointer copying behavior (/certora/tutorials-code/memorytests/test17.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of pointer-to-pointer behavior
 *
 * This contract accepts a dynamic memory array, a value and an index to perform assignment operation.
 * The function assigns a value to dynamic array at given index and returns a memory array for the purpose of validating the assignment behavior.
 *
 */
contract test17 {
   
    constructor() {
    }

 function assign2(uint8[] memory x, uint8 i, uint8 y) 
    public 
    returns (uint8[] memory)  
    {
      x[i] = y;
      return x;
    }

   }
