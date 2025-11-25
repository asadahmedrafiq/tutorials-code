
    // SPDX-License-Identifier: MIT
// Test for single level aliasing for dynamic memory array (singlealiasingdynamicd2.sol).
 /**Test configurations: 
 *  #Dimensions (D) : 2D
 *   Size       (n) : NA
 *   Single Aliasing: Yes
 *   Double Aliasing: No
 */
pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract singlealiasingdynamicd2 {
   
  constructor() {
  }

  function singlealiasingdynamicd2f(uint8[][] memory x, uint8 i, uint8 j, uint8 k, uint8 value, uint8[][] memory y ) 
    pure
    external 
    returns (uint8[][] memory)  
    {
     x [i] = y [j];
      y [j][k] = value;
      return x;
    }

}
