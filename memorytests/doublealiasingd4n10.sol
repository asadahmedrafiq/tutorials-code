// SPDX-License-Identifier: MIT
// Test for double aliasing behavior of memory arrays(doublealiasingd4n10.sol).

pragma solidity ^0.8.25;
 /**Test configurations: 
 *  #Dimensions (D) : D = 4
 *   Size       (n) : n = 10
 *   Single Aliasing: No
 *   Double Aliasing: Yes
 */

/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract doublealiasingd4n10 {
   
  constructor() {
  }

  function doublealiasingd4n10f(uint8[10][10][10][10] memory x, uint8 i, uint8 j, uint8 k, uint8 l, uint8 m, uint8 n, uint8 o, uint8 value, uint8[10][10][10][10] memory y, uint8[10][10][10][10] memory z) 
    pure
    external 
    returns (uint8[10][10][10][10] memory)  
    {
      x [i] = z [j];
      z [j][k] = y [l][m];
      y [l][m][n][o] = value;
      return x;
    }
}