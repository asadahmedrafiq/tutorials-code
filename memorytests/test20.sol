// SPDX-License-Identifier: MIT
// Memory test for pointer-to-pointer copyingbehavior (/certora/tutorials-code/memorytests/test20.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior in multi-dimenstional memory arrays
 *
 * This contract accepts three static two-dimensional memory arrays and indeces to perform assignment operation.
 * Furhter one of the array data/content is loaded. This then serves us to obse3rve the behavior of the memory assignment of such arrays.
 * The function does assignment operation and returns one of the memory array for the purpose of validating the assignment behavior.
 *
 */
contract test20 {
   
    constructor() {
    }

  function daliasing1(uint8[][] memory x8, uint8 i8, uint8 j8, uint8 k8, uint8 value8, uint8[][] memory y8) 
    public 
    returns (uint8[][] memory)  
    {
     x8[i8] = y8[j8];
      y8[j8][k8] = value8;
      return x8;
    }

   }
