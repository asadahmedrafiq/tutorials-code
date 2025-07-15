// SPDX-License-Identifier: MIT
// Memory test for pointer-to-pointer copyingbehavior (/certora/tutorials-code/memorytests/p2p.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of pointer-to-pointer behavior
 *
 * This contract accepts two static memory array and indeces to perform assignment operation.
 * The function does assignment operation and returns one of the memory array for the purpose of validating the assignment behavior.
 *
 */
contract memorytest2 {
   
    constructor() {
    }

 function assign2(uint8[5] memory x, uint8 i, uint8 j, uint8[5] memory y) public returns (uint8[5] memory)  {
      x[i] = y[j];
      return x;
    }

   }
