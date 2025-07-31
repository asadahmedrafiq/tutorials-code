// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/tests.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract tests {
   
    constructor() {
    }

// assign1 function assess the value assignment to a pointer behavior of memory variables in Solidity.
// assign1 accepts a memory array of fixed size, index and value.
// It returns memroty array after value assignment to a pointer operation.

 function assign1(uint8[5] memory x, uint8 i, uint8 y) 
    public 
    returns (uint8[50] memory)  
    {
      x[i] = y;
      return x;
    }

// assign2 function is similar to assign1.
// Only difference is size of the fixed-sized array.
// assign2 is designed to assess the affect of size of the array in relation to verification effort in Certora

    function assign2(uint8[50] memory x, uint8 i, uint8 y) 
    public 
    returns (uint8[50] memory)  
    {
      x[i] = y;
      return x;
    }

// assign3 is an implementation of aliasing using two-dimensional fixed sized array.
// Only difference is dimension of the fixed-sized arrays.
// assign3 accepts two dimensional fixed sized arrays , their respective indices and value.
// The test invovlves the pointer-to-pointe assignment followed by the value-to-pointer assignemnt.

  function assign3(uint8[5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[5][5] memory y) 
    public 
    returns (uint8[5][5] memory)  
    {
      x[i] = y[j];
      y[j][k] = value;
      return x;
    }

// assign4 function is similar to assign3.
// Only difference is the size of two-dimanesional fixed sized arrays.

    function assign4(uint8[50][50] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[50][50] memory y) 
    public 
    returns (uint8[50][50] memory)  
    {
      x[i] = y[j];
      y[j][k] = value;
      return x;
    }

// assign5 is an implemntation of aliasing using three-dimensional fixed sized arrays.
// assign5 accepts three arrays which are three dimensional arrays, respective indices and a value.
// The function performs a pointer-to-pointer operation on the given martrices and then assign value to the one of the arrays.
 function assign5(uint8[5][5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 l, uint8 m, uint8 n, uint8 value, uint8[5][5][5] memory y, uint8[5][5][5] memory z) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x[i] = y[j];
      y[j][k] = z[l][m];
      z[l][m][n]= value;
      return x;
    }

// assign6 is same as assign5.
// Only difference is the size of the given matrices to guage the effect on the verification effort in Certora.

 function assign6(uint8[50][50][50] memory x, uint8 i, uint8 j, uint8 k, uint8 l, uint8 m, uint8 n, uint8 value, uint8[50][50][50] memory y, uint8[5][5][5] memory z) 
    public 
    returns (uint8[50][50][50] memory)  
    {
      x[i] = y[j];
      y[j][k] = z[l][m];
      z[l][m][n]= value;
      return x;
    }

 // assign7 is a function that accepts a dynamic memory array, performs an value-to-pointer assignment  operations and rerutrns 
 // the dynamic array. 
 // The function is design to test Certora verification of dynamic arrays

 function assign7(uint8[] memory x, uint8 i, uint8 y) 
    public 
    returns (uint8[] memory)  
    {
      x[i] = y;
      return x;
    }

 // assign8 is same as assign7.
 // Only difference is the dimensions of the memory arrays. 
  
 function assign8(uint8[][] memory x, uint8 i, uint8 j, uint8[][] y) 
    public 
    returns (uint8[][] memory)  
    {
     x[i] = y[j];
      y[j][k] = value;
      return x;
    }


   }
