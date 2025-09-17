// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test04.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test04 {
   
    constructor() {
    }

// assign22 is same as assign2  in functionality.
// Only difference is size of the fixed-sized array.
// assign  is designed to assess the affect of size of the array in relation to verification effort in Certora

    function t04(uint8[20]memory x, uint8 i, uint8 j, uint8 value, uint8[20] memory y ) 
    pure
    public 
    returns (uint8[20] memory)  
    {
      x [i] = y [j];
      y [j]= value;
      return x;
    }
}