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
contract v2p {
   
    constructor() {
    }

 function assign1(uint8[5] memory x, uint8 i, uint8 y) 
    public 
    returns (uint8[50] memory)  
    {
      x[i] = y;
      return x;
    }

    function assign2(uint8[50] memory x, uint8 i, uint8 y) 
    public 
    returns (uint8[50] memory)  
    {
      x[i] = y;
      return x;
    }

  function assign3(uint8[5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[5][5] memory y) 
    public 
    returns (uint8[5][5] memory)  
    {
      x[i] = y[j];
      y[j][k] = value;
      return x;
    }

    function assign4(uint8[50][50] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[50][50] memory y) 
    public 
    returns (uint8[50][50] memory)  
    {
      x[i] = y[j];
      y[j][k] = value;
      return x;
    }


 function assign5(uint8[5][5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 l, uint8 m, uint8 n, uint8 value, uint8[5][5][5] memory y, uint8[5][5][5] memory z) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x[i] = y[j];
      y[j][k] = z[l][m];
      z[l][m][n]= value;
      return x;
    }


 function assign6(uint8[50][50][50] memory x, uint8 i, uint8 j, uint8 k, uint8 l, uint8 m, uint8 n, uint8 value, uint8[50][50][50] memory y, uint8[5][5][5] memory z) 
    public 
    returns (uint8[50][50][50] memory)  
    {
      x[i] = y[j];
      y[j][k] = z[l][m];
      z[l][m][n]= value;
      return x;
    }

    
 function assign7(uint8[] memory x, uint8 i, uint8 y) 
    public 
    returns (uint8[] memory)  
    {
      x[i] = y;
      return x;
    }

  
 function assign7(uint8[][] memory x, uint8 i, uint8 j, uint8[][] y) 
    public 
    returns (uint8[][] memory)  
    {
     x[i] = y[j];
      y[j][k] = value;
      return x;
    }


   }
