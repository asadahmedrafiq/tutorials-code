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

 function assign1(uint8[5] memory x1, uint8 i1, uint8 y1) 
    public 
    returns (uint8[5] memory)  
    {
      x1[i1] = y1;
      return x1;
    }

// assign2 function is similar to assign1.
// Only difference is size of the fixed-sized array.
// assign2 is designed to assess the affect of size of the array in relation to verification effort in Certora

    function assign2(uint8[20] memory x2, uint8 i2, uint8 y2) 
    public 
    returns (uint8[20] memory)  
    {
      x2[i2] = y2;
      return x2;
    }

function assign21(uint8[5]memory x31, uint8 i31, uint8 j31, uint8 value31, uint8[5] memory y31) 
    public 
    returns (uint8[5] memory)  
    {
      x31[i31] = y31[j31];
      y31[j31]= value31;
      return x31;
    }

    function assign22(uint8[20]memory x32, uint8 i32, uint8 j32, uint8 value32, uint8[20] memory y32) 
    public 
    returns (uint8[20] memory)  
    {
      x32[i32] = y32[j32];
      y32[j32]= value32;
      return x32;
    }
    
// assign3 is an implementation of aliasing using two-dimensional fixed sized array.
// Only difference is dimension of the fixed-sized arrays.
// assign3 accepts two dimensional fixed sized arrays , their respective indices and value.
// The test invovlves the pointer-to-pointe assignment followed by the value-to-pointer assignemnt.

  function assign3(uint8[5][5] memory x3, uint8 i3, uint8 j3, uint8 k3, uint8 value3, uint8[5][5] memory y3) 
    public 
    returns (uint8[5][5] memory)  
    {
      x3[i3] = y3[j3];
      y3[j3][k3] = value3;
      return x3;
    }

// assign4 function is similar to assign3.
// Only difference is the size of two-dimanesional fixed sized arrays.

    function assign4(uint8[20][20] memory x4, uint8 i4, uint8 j4, uint8 k4, uint8 value4, uint8[20][20] memory y4) 
    public 
    returns (uint8[20][20] memory)  
    {
      x4[i4] = y4[j4];
      y4[j4][k4] = value4;
      return x4;
    }

// assign5 is an implemntation of aliasing using three-dimensional fixed sized arrays.
// assign5 accepts three arrays which are three dimensional arrays, respective indices and a value.
// The function performs a pointer-to-pointer operation on the given martrices and then assign value to the one of the arrays.
 function assign5(uint8[5][5][5] memory x5, uint8 i5, uint8 j5, uint8 k5, uint8 l5, uint8 m5, uint8 n5, uint8 value5, uint8[5][5][5] memory y5, uint8[5][5][5] memory z5) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x5[i5] = y5[j5];
      y5[j5][k5] = z5[l5][m5];
      z5[l5][m5][n5]= value5;
      return x5;
    }

// assign6 is same as assign5.
// Only difference is the size of the given matrices to guage the effect on the verification effort in Certora.

 function assign6(uint8[50][50][50] memory x6, uint8 i6, uint8 j6, uint8 k6, uint8 l6, uint8 m6, uint8 n6, uint8 value6, uint8[50][50][50] memory y6, uint8[50][50][50] memory z6) 
    public 
    returns (uint8[50][50][50] memory)  
    {
      x6[i6] = y6[j6];
      y6[j6][k6] = z6[l6][m6];
      z6[l6][m6][n6]= value6;
      return x6;
    }

 // assign7 is a function that accepts a dynamic memory array, performs an value-to-pointer assignment  operations and rerutrns 
 // the dynamic array. 
 // The function is design to test Certora verification of dynamic arrays

 function assign7(uint8[] memory x7, uint8 i7, uint8 y7) 
    public 
    returns (uint8[] memory)  
    {
      x7[i7] = y7;
      return x7;
    }

 // assign8 is same as assign7.
 // Only difference is the dimensions of the memory arrays. 
  
 function assign8(uint8[][] memory x8, uint8 i8, uint8 j8, uint8 k8, uint8 value8, uint8[][] memory y8) 
    public 
    returns (uint8[][] memory)  
    {
     x8[i8] = y8[j8];
      y8[j8][k8] = value8;
      return x8;
    }


   }
