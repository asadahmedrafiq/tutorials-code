// SPDX-License-Identifier: MIT
// Test for value-to-memory array assignment behavior  (assignd3n10.sol).

pragma solidity ^0.8.25;
/**Test configurations: 
 *  #Dimensions (D) : D = 3
 *   Size       (n) : n = 10
 *   Single Aliasing: No 
 *   Double Aliasing: No
 */

/**
 * @dev Implementation of assignment behavior of memory variables in Solidity
 */
contract assignd3n10 {
   
  constructor() {
  }


  function assignd3n10f(uint8[10][10][10] memory x, uint8 i, uint8 j, uint8 k, uint8 y) 
    pure
    external 
    returns (uint8[10][10][10] memory)  
    {
      x [i][j][k] = y;
      return x;
    }

}