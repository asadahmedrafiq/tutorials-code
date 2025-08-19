// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test05.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test05 {
   
    constructor() {
    }

// assign3 is a test function which verifies the value assignment to a 3D memory array (pointer) in Certora.
// assign3 accepts a 3D memory array of fixed size (x3), indeces (i3, j3 and k3) and value (y3).
// It returns memroty array, x3, after value assignment to a pointer operation.


function t05(uint8[5][5][5] memory x3, uint8 i3, uint8 j3, uint8 k3, uint8 y3) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x3[i3][j3][k3] = y3;
      return x3;
    }

}