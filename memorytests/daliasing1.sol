// SPDX-License-Identifier: MIT
// Memory test for pointer-to-pointer copying behavior fo dynamic memory lists(/certora/tutorials-code/memorytests/daliasing1.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior in multi-dimenstional dynamic memory arrays
 *
 * This contract accepts two dynamic two-dimensional memory arrays and indeces to perform assignment operation.
 * Furhter one of the array data/content is loaded. This then serves us to obse3rve the behavior of the memory assignment of such arrays.
 * The function does assignment operation and returns one of the memory array for the purpose of validating the assignment behavior.
 *
 */
contract daliasing1 {
   
    constructor() {
    }

 function assign3(uint8[][] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[][] memory y) 
    public 
    returns (uint8[][] memory)  
    {
      x[i] = y[j];
      y[j][k] = value;
      return x;
    }

   }
