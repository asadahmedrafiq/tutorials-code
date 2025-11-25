// SPDX-License-Identifier: MIT
// Test for single level aliasing for memory array (singlealiasingd2n20.sol).
pragma solidity ^0.8.25;
 /**Test configurations: 
 *  #Dimensions (D) : D = 2
 *   Size       (n) : n = 20
 *   Single Aliasing: Yes
 *   Double Aliasing: No
 */

/**
 * @dev Implementation of assignment behavior of memory variables in Solidity
 */
contract singlealiasingd2n20 {
   
  constructor() {
  }

  function singlealiasingd2n20f(uint8[20][20] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[20][20] memory y ) 
    pure
    external 
    returns (uint8[20][20] memory)  
    {
      x [i] = y [j];
      y [j][k] = value;
      return x;
    }

}