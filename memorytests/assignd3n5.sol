// SPDX-License-Identifier: MIT
// Test for value-to-memory array assignment behavior  (assignd3n5.sol).

pragma solidity ^0.8.25;

/**Test configurations: 
 *  #Dimensions (D) : D = 3
 *   Size       (n) : n = 5
 *   Single Aliasing: No 
 *   Double Aliasing: No
 */
/**
 * @dev Implementation of assignment behavior of memory variables in Solidity
 */
contract assignd3n5 {
   
  constructor() {
  }

  function assignd3n5f(uint8[5][5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 y ) 
    pure
    external 
    returns (uint8[5][5][5] memory)  
    {
      x [i][j][k] = y;
      return x;
    }

}
