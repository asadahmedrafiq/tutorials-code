// SPDX-License-Identifier: MIT
// Test for value-to-memory array assignment behavior (assignd1n5.sol).

 /**Test configurations: 
 *  #Dimensions (D) : D = 1
 *   Size       (n) : n = 5
 *   Single Aliasing: No 
 *   Double Aliasing: No
 */
pragma solidity ^0.8.25;

contract assignd1n5 {
   
   constructor() {
   }

   function assignd1n5f(uint8[5] memory x, uint8 i, uint8 y) 
      pure
      external 
      returns (uint8[5] memory) {
      x[i] = y;
      return x;
    }

}