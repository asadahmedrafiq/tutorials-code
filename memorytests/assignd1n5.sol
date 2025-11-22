// SPDX-License-Identifier: MIT
// Memory test for assignment behavior test01.sol

pragma solidity ^0.8.25;

contract test01 {
   
   constructor() {
   }

   function t01(uint8[5] memory x, uint8 i, uint8 y) 
      pure
      external 
      returns (uint8[5] memory) {
      x[i] = y;
      return x;
    }

}