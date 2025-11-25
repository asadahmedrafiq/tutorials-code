// SPDX-License-Identifier: MIT
// Test for value-to-memory array assignment behavior (assignd1n20.sol).

 /**Test results:
 *  #Dimensions (D) : D = 1
 *   Size       (n) : n = 20
 *   Single Aliasing: No 
 *   Double Aliasing: No
 */


pragma solidity ^0.8.25;

contract assignd1n20 {
   
  constructor() {
  }

  function assignd1n20f(uint8[20] memory x, uint8 i, uint8 y) 
    pure
    external 
    returns (uint8[20] memory)  
    {
      x[i] = y;
      return x;
    }
}