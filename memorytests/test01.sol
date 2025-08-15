// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/test01.sol)

pragma solidity ^0.8.25;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract test01 {
   
    constructor() {
    }


// assign1 function assess the value assignment to a pointer behavior of memory variables in Solidity.
// assign1 accepts a memory array of fixed size, an index and a value.
// It returns memroy array after value-to-pointer assignment operation.

 function assign1(uint8[5] memory x1, uint8 i1, uint8 y1) 
    public 
    returns (uint8[5] memory)  
    {
      x1[i1] = y1;
      return x1;
    }

}