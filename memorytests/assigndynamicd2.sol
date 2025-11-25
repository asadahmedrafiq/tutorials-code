// SPDX-License-Identifier: MIT
// Test for value-to-assignment behavior of dynamic memory array (assigndynamicd2.sol).

pragma solidity ^0.8.25;

 /**Test configurations: 
 *  #Dimensions (D) : D = 2
 *   Size       (n) : NA
 *   Single Aliasing: No
 *   Double Aliasing: No
 */
/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract assigndynamicd2 {
   
  constructor() {
  }

  function assigndynamicd2f(uint8[][] memory x, uint8 i, uint8 j, uint8 value) 
    pure
    external 
    returns (uint8[][] memory)  
    {
        x [i][j] = value;
      return x;
    }

}