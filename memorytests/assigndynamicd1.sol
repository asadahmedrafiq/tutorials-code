
    // SPDX-License-Identifier: MIT
// Test for value-to-assignment behavior of dynamic memory array (assigndynamicd1.sol).

pragma solidity ^0.8.25;
 /**Test configurations: 
 *     Dimension (D): 1
 * Dynamic (n bound): Yes (200 > n > 0)
 *         loop_iter: 200
 *   Single Aliasing: No
 *   Double Aliasing: No
 */

/**
 * @dev Implementation of assignment behavior of dynamicla memory variables in Solidity
 */
contract assigndynamicd1 {
   
    constructor() {
    }

 function assigndynamicd1f(uint8[] memory x, uint8 i, uint8 y) 
    pure
    public 
    returns (uint8[] memory)  
    {
      x [i] = y;
      return x;
    }
}
