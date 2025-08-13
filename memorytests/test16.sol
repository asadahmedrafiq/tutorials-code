
    // SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test16.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test16 {
   
    constructor() {
    }

 function assign2ddaliasing(uint8[5][5] memory x6, uint8 i6, uint8 j6, uint8 k6,  uint8 l6, uint8 value6, uint8[5][5] memory y6, uint8[5][5] memory z6) 
    public 
    returns (uint8[5][5] memory)  
    {
      x6[i6] = y6[j6];
      y6[j6] = z6[k6];
      z6[k6][l6] = value6;
      return x6;
    }
}
