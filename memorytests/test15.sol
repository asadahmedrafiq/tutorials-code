
    // SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test15.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test15 {
   
    constructor() {
    }

 function assign2dp2psize(uint8[50][50] memory x6, uint8 i6, uint8 j6, uint8 k6, uint8 value6, uint8[50][50] memory y6) 
    public 
    returns (uint8[50][50] memory)  
    {
      x6[i6] = y6[j6];
      y6[j6][k6] = value6;
      return x6;
    }
}
