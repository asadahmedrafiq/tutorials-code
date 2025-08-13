// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test11.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test11 {
   
    constructor() {
    }
// assign3dda is an implemntation of aliasing using three-dimensional fixed sized arrays.
// assign3dda accepts three arrays which are three dimensional arrays, respective indices and a value.
// The function performs a pointer-to-pointer operation on the given martrices and then assign value to the one of the arrays.
 function assign3dda(uint8[5][5][5] memory x8, uint8 i8, uint8 j8, uint8 k8, uint8 l8, uint8 m8, uint8 n8, uint8 value8, uint8[5][5][5] memory y8, uint8[5][5][5] memory z8) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x8[i8] = y8[j8];
      y8[j8][k8] = z8[l8][m8];
      z8[l8][m8][n8]= value8;
      return x8;
    }
}