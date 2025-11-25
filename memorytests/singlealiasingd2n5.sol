// SPDX-License-Identifier: MIT
// Test for single level aliasing for memory array (singlealiasingd2n5.sol).

pragma solidity ^0.8.25;
 /**Test configurations: 
 *  #Dimensions (D) : D = 3
 *   Size       (n) : n = 5
 *   Single Aliasing: No
 *   Double Aliasing: Yes
 */

/**
 * @dev Implementation of assignment behavior of memory variables in Solidity
 */
contract singlealiasingd2n5 {
   
  constructor() {
  }

  function singlealiasingd2n5f(uint8[5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[5][5] memory y ) 
    pure
    external 
    returns (uint8[5][5] memory)  
    {
      x [i] = y [j];
      y [j][k] = value;
      return x;
    }

}