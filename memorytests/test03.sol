// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test03.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test03 {
   
  constructor() {
    }


  function t03 ( uint8[5] memory x, uint8 i, uint8 j, uint8 value, uint8[5] memory y ) 
    pure
    public 
    returns (uint8[5] memory) {
      x [i] = y [j];
      y [j]= value ;
      return x ;
    }
}