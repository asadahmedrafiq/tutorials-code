// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test02.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test04 {
   
    constructor() {
    }

// assign22 is same as assign2  in functionality.
// Only difference is size of the fixed-sized array.
// assign22 is designed to assess the affect of size of the array in relation to verification effort in Certora

    function assign22(uint8[20]memory x22, uint8 i22, uint8 j22, uint8 value22, uint8[20] memory y22) 
    public 
    returns (uint8[20] memory)  
    {
      x22[i22] = y22[j22];
      y22[j22]= value22;
      return x22;
    }
}