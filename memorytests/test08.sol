// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test08.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test08 {
   
    constructor() {
    }
// assign4dp2p is a test function which verifies the pointer to pointer array for 4D memory arrays in Certora.
// assign4dp2p accepts a 4D memory array of fixed size (x51), indeces (i51, j51, k51, l51 and m51) and value (value5).
// It returns memroty array, x51, after value to apointer assignment operation.


function assign4dp2p(uint8[5][5][5][5] memory x51, uint8 i51, uint8 j51, uint8 k51, uint8 l51, uint8 m51, uint8 value51, uint8[5][5][5][5] memory y51) 
    public 
    returns (uint8[5][5][5][5] memory)  
    {
      x51[i51] = y51[j51];
      y51[j51][k51][l51][m51] = value51;
      return x51;
    }

}