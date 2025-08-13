// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test07.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test07 {
   
    constructor() {
    }

// assign4dvp is a test function which verifies the assignment to pointer array for 4D memory arrays in Certora.
// assign4dvp accepts a 4D memory array of fixed size (x5), indeces (i5, j5, k5 and l5) and value (value5).
// It returns memroty array, x5, after value to apointer assignment operation.

function assign4dvp(uint8[5][5][5][5] memory x5, uint8 i5, uint8 j5, uint8 k5, uint8 l5, uint8 value5) 
    public 
    returns (uint8[5][5][5][5] memory)  
    {
      x5[i5][j5][k5][l5] = value5;
      return x5;
    }


}