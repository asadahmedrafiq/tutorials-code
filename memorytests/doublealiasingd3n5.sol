// SPDX-License-Identifier: MIT
// Test for double aliasing behavior of memory arrays (doublealiasingd3n5.sol).

pragma solidity ^0.8.25;
 /**Test configurations: 
 *  #Dimensions (D) : D = 3
 *   Size       (n) : n = 5
 *   Single Aliasing: No
 *   Double Aliasing: Yes
 */

/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract doublealiasingd3n5 {
   
  constructor() {
  }

  function doublealiasingd3n5f(uint8[5][5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 l, uint8 m, uint8 n, uint8 value, uint8[5][5][5] memory y , uint8[5][5][5] memory z ) 
    pure
    external 
    returns (uint8[5][5][5] memory)  
    {
      x [i] = y [j];
      y [j][k] = z [l][m];
      z [l][m][n] = value;
      return x;
    }

}