// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/tests.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract testsv2 {
   
    constructor() {
    }

// assign1 is a test function which verifies the value assignment to a memory array (pointer) in Certora.
// assign1 accepts a memory array of fixed size (x1), index (i1) and value (y1).
// It returns memroty array, x1, after value assignment to a pointer operation.

 function assign1(uint8[5] memory x1, uint8 i1, uint8 y1) 
    public 
    returns (uint8[5] memory)  
    {
      x1[i1] = y1;
      return x1;
    }

// assign12 function is similar to assign1.
// Only difference is size of the fixed-sized array.
// assign12 is designed to assess the affect of size of the array in relation to verification effort in Certora

    function assign12(uint8[20] memory x12, uint8 i12, uint8 y12) 
    public 
    returns (uint8[20] memory)  
    {
      x12[i12] = y12;
      return x12;
    }

// assign2 is a test function which verifies the assignment of a memory array (pointer)  to another memory array pointer in Certora.
// assign2 accepts a memory array of fixed size (x2), indeces (i2 and j2), value (value2) and y2.
// It returns memroty array, x2, after pointer to pointer and value to a pointer assignment operations, respectively.


function assign2(uint8[5]memory x2, uint8 i2, uint8 j2, uint8 value2, uint8[5] memory y2) 
    public 
    returns (uint8[5] memory)  
    {
      x2[i2] = y2[j2];
      y2[j2]= value2;
      return x2;
    }

// assign22 is same as assign2  in functionality.
// Only difference is size of the fixed-sized array.
// assign22 is designed to assess the affect of size of the array in relation to verification effort in Certora

    function assign22(uint8[20]memory x22, uint8 i22, uint8 j22, uint8 value22, uint8[20] memory y22) 
    public 
    returns (uint8[20] memory)  
    {
      x22[i22] = y22[j22];
      y22[j22]= value22;
      return x22;
    }

// assign3 is a test function which verifies the value assignment to a 3D memory array (pointer) in Certora.
// assign3 accepts a 3D memory array of fixed size (x3), indeces (i3, j3 and k3) and value (y3).
// It returns memroty array, x3, after value assignment to a pointer operation.


function assign3(uint8[5][5][5] memory x3, uint8 i3, uint8 j3, uint8 k3, uint8 y3) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x3[i3][j3][k3] = y3;
      return x3;
    }

// assign4 is a test function which verifies the pointer to pointer array for 3D memory arrays in Certora.
// assign4 accepts a 3D memory array of fixed size (x4), indeces (i4, j4, k4 and l4), value (value4) and y4 3D memory.
// It returns memroty array, x3, after pointer to a pointer and value assignment operation, respectively.


 function assign4(uint8[5][5][5] memory x4, uint8 i4, uint8 j4, uint8 k4, uint8 l4, uint8 value4, uint8[5][5][5] memory y4) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x4[i4] = y4[j4];
      y4[j4][k4][l4] = value4;
      return x4;
    }

// assign5 is a test function which verifies the assignment to pointer array for 4D memory arrays in Certora.
// assign5 accepts a 4D memory array of fixed size (x5), indeces (i5, j5, k5 and l5) and value (value5).
// It returns memroty array, x3, after value to apointer assignment operation.

function assign5(uint8[5][5][5][5] memory x5, uint8 i5, uint8 j5, uint8 k5, uint8 l5, uint8 value5) 
    public 
    returns (uint8[5][5][5][5] memory)  
    {
      x5[i5][j5][k5][l5] = value5;
      return x5;
    }


// assign51 is a test function which verifies the pointer to pointer array for 4D memory arrays in Certora.
// assign51 accepts a 4D memory array of fixed size (x5), indeces (i5, j5, k5 and l5) and value (value5).
// It returns memroty array, x3, after value to apointer assignment operation.

function assign51(uint8[10][10][10][10] memory x51, uint8 i51, uint8 j51, uint8 k51, uint8 l51, uint8 m51, uint8 value51, uint8[10][10][10][10] memory y51) 
    public 
    returns (uint8[10][10][10][10] memory)  
    {
      x51[i51] = y51[j51];
      y51[j51][k51][l51][m51] = value51;
      return x51;
    }

// assign6 is an implementation of aliasing using two-dimensional fixed sized array.
// assign6 accepts two dimensional fixed sized arrays , their respective indices and value.
// The test invovlves the pointer-to-pointe assignment followed by the value-to-pointer assignemnt.

  function assign6(uint8[5][5] memory x6, uint8 i6, uint8 j6, uint8 k6, uint8 value6, uint8[5][5] memory y6) 
    public 
    returns (uint8[5][5] memory)  
    {
      x6[i6] = y6[j6];
      y6[j6][k6] = value6;
      return x6;
    }

// assign7 function is similar to assign6.
// Only difference is the size of two-dimanesional fixed sized arrays.

    function assign7(uint8 [10][10] memory x7, uint8 i7, uint8 j7, uint8 k7, uint8 value7, uint8[10][10] memory y7) 
    public 
    returns (uint8[10][10] memory)  
    {
      x7[i7] = y7[j7];
      y7[j7][k7] = value7;
      return x7;
    }

// assign8 is an implemntation of aliasing using three-dimensional fixed sized arrays.
// assign8 accepts three arrays which are three dimensional arrays, respective indices and a value.
// The function performs a pointer-to-pointer operation on the given martrices and then assign value to the one of the arrays.
 function assign8(uint8[5][5][5] memory x8, uint8 i8, uint8 j8, uint8 k8, uint8 l8, uint8 m8, uint8 n8, uint8 value8, uint8[5][5][5] memory y8, uint8[5][5][5] memory z8) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x8[i8] = y8[j8];
      y8[j8][k8] = z8[l8][m8];
      z8l8][m8][n8]= value8;
      return x8;
    }
//assign9 returns rhs. So can be usewd to check the aliasing of rhs.
function assign9(uint8[5][5][5] memory x9, uint8 i9, uint8 j9, uint8 k9, uint8 l9, uint8 m9, uint8 n9, uint8 value9, uint8[5][5][5] memory y9, uint8[5][5][5] memory z9) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x9[i9] = y9[j9];
      y9[j9][k9] = z9[l9][m9];
      z9[l9][m9][n9]= value9;
      return y9;
    }

// assign91 is same as assign9.
// Only difference is the size of the given matrices to guage the effect on the verification effort in Certora.

 function assign91(uint8[10][10][10] memory x91, uint8 i91, uint8 j91, uint8 k91, uint8 l91, uint8 m91, uint8 n91, uint8 value91, uint8[10][10][10] memory y91, uint8[10][10][10] memory z91) 
    public 
    returns (uint8[10][10][10] memory)  
    {
      x6[i6] = y6[j6];
      y6[j6][k6] = z6[l6][m6];
      z6[l6][m6][n6]= value6;
      return x6;
    }

 function assign4d(uint8[5][5][5][5] memory x4d, uint8 i4d, uint8 j4d, uint8 k4d, uint8 l4d, uint8 m4d, uint8 n4d, uint8 o, uint8 p,  uint8 q,  uint8 q, uint8 value4d, uint8[5][5][5][5] memory y4d, uint8[5][5][5][5] memory t1, uint8[5][5][5][5] memory t12) 
    public 
    returns (uint8[5][5][5][5] memory)  
    {
      x4d[i4d] = y4d[j4d];
      y5[j4d][k4d] = t1[l4d][m4d];
      t1[l4d][m4d][n4d]= t2[n][o][p];
      t2[n][o][p][q] = value10;
      return x4d;
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

function assign61(uint8[][][] memory x61, uint8 i61, uint8 j61, uint8 k61, uint8 l61, uint8 m61, uint8 n61, uint8 value61, uint8[][][] memory y61, uint8[][][] memory z61) 
    public 
    returns (uint8[][][] memory)  
    {
      x61[i61] = y61[j61];
      y61[j61][k61] = z61[l61][m61];
      z61[l61][m61][n61]= value61;
      return x61;
    }

 
   }
