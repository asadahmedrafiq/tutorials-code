// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test24.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test24 {
   
    constructor() {
    }
// assign3dda is an implemntation of aliasing using three-dimensional fixed sized arrays.
// assign3dda accepts three arrays which are three dimensional arrays, respective indices and a value.
// The function performs a pointer-to-pointer operation on the given martrices and then assign value to the one of the arrays.
 function t24(uint8[10][10][10][10] memory x8, uint8 i8, uint8 j8, uint8 k8, uint8 l8, uint8 m8, uint8 n8, uint8 o8, uint8 value8, uint8[10][10][10][10] memory y8, uint8[10][10][10][10] memory z8) 
    public 
    returns (uint8[10][10][10][10] memory)  
    {
      x8[i8] = z8[j8];
      z8[j8][k8] = y8[l8][m8];
      y8[l8][m8][n8][o8]= value8;
      return x8;
    }
}