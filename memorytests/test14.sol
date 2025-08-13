
    // SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test14.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test14 {
   
    constructor() {
    }
// assigndyvtp is a function that accepts a dynamic memory array, performs an value-to-pointer assignment  operations and rerutrns 
 // the dynamic array. 
 // The function is design to test Certora verification of dynamic arrays

 function assigndy2dptp(uint8[][] memory x8, uint8 i8, uint8 j8, uint8 k8, uint8 value8, uint8[][] memory y8) 
    public 
    returns (uint8[][] memory)  
    {
     x8[i8] = y8[j8];
      y8[j8][k8] = value8;
      return x8;
    }

}
