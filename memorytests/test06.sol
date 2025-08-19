// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test06.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test06 {
   
    constructor() {
    }

// assign31 is a test function which verifies the pointer to pointer array for 3D memory arrays in Certora.
// assign31 accepts a 3D memory array of fixed size (x4), indeces (i4, j4, k4 and l4), value (value4) and y4 3D memory.
// It returns memroty array, x3, after pointer to a pointer and value assignment operation, respectively.


 function t06(uint8[5][5][5] memory x4, uint8 i4, uint8 j4, uint8 k4, uint8 l4, uint8 value4, uint8[5][5][5] memory y4) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x4[i4] = y4[j4];
      y4[j4][k4][l4] = value4;
      return x4;
    }

}