// SPDX-License-Identifier: MIT
// Test for value-to-memory array assignment behavior (assignd2n5.sol).

 /**Test configurations: 
 *  #Dimensions (D) : D = 2
 *   Size       (n) : n = 5
 *   Single Aliasing: No 
 *   Double Aliasing: No
 */
pragma solidity ^0.8.25;

contract assignd2n5 {
   
  constructor() {
    }


  function assignd2n5f(uint8[5][5] memory x, uint8 i, uint8 j, uint8 value) 
    pure
    external 
    returns (uint8[5][5] memory)  
    {
        x [i][j] = value;
      return x;
    }

}