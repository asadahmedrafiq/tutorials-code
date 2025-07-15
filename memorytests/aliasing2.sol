// SPDX-License-Identifier: MIT
// Memory test for pointer-to-pointer copyingbehavior (/certora/tutorials-code/memorytests/aliasing2.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior in multi-dimenstional memory arrays
 *
 * This contract accepts three static two-dimensional memory arrays and indeces to perform assignment operation.
 * Furhter one of the array data/content is loaded. This then serves us to obse3rve the behavior of the memory assignment of such arrays.
 * The function does assignment operation and returns one of the memory array for the purpose of validating the assignment behavior.
 *
 */
contract aliasing2 {
   
    constructor() {
    }

 function assign4(uint8[5][5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 l, uint8 m, uint8 n, uint8 value, uint8[5][5][5] memory y, uint8[5][5][5] memory z) 
    public 
    returns (uint8[5][5][5] memory)  
    {
      x[i] = y[j];
      y[j][k] = z[l][m];
      z[l][m][n]= value;
      return x;
    }

   }
