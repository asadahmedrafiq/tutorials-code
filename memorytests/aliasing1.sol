// SPDX-License-Identifier: MIT
// Memory test for pointer-to-pointer copyingbehavior (/certora/tutorials-code/memorytests/aliasing1.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior in multi-dimenstionalstatic  memory arrays
 *
 * This contract accepts two static two-dimensional memory arrays and respective indeces to perform assignment operation.
 * In first step, a memory pointer-to-pointer assignment is performed. In the second step, source memory array data is updated 
 * at that specific pointer location with value.
 * The destenation array is returned which should reflect changes made in the second step due to first step.
 *
 */
contract aliasing1 {
   
    constructor() {
    }

 function assign3(uint8[50][50] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[50][50] memory y) 
    public 
    returns (uint8[50][50] memory)  
    {
      x[i] = y[j];
      y[j][k] = value;
      return x;
    }

   }
