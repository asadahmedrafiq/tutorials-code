
    // SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test12.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test12 {
   
    constructor() {
    }
// test12.sol is same as test11.
// Only difference is the size of the given matrices to guage the effect on the verification effort in Certora.
function t12(uint8[10][10][10] memory x91, uint8 i91, uint8 j91, uint8 k91, uint8 l91, uint8 m91, uint8 n91, uint8 value91, uint8[10][10][10] memory y91, uint8[10][10][10] memory z91) 
    public 
    returns (uint8[10][10][10] memory)  
    {
      x91[i91] = y91[j91];
      y91[j91][k91] = z91[l91][m91];
      z91[l91][m91][n91]= value91;
      return x91;
    }
}