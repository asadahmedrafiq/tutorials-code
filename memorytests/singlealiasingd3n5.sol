// SPDX-License-Identifier: MIT
// Test for single level aliasing for memory array (singlealiasingd3n5.sol).
 /**Test configurations: 
 *  #Dimensions (D) : 3
 *   Size       (n) : 5
 *   Single Aliasing: Yes
 *   Double Aliasing: No
 */
pragma solidity ^0.8.25;

/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract singlealiasingd3n5 {
   
  constructor() {
    }

  function singlealiasingd3n5f(uint8[5][5][5] memory x, uint8 i, uint8 j, uint8 k, uint8 l, uint8 value, uint8[5][5][5] memory y ) 
    pure
    external 
    returns (uint8[5][5][5] memory)  
    {
      x [i] = y [j];
      y [j][k][l] = value;
      return x;
    }

}