// SPDX-License-Identifier: GPL-3.0
// Test for initializing of memory array (initializationd1n1.sol). 
pragma solidity >=0.8.25;
  /**Test configurations: 1
 *  #Dimensions (D) : D = 1
 *   Size       (n) : n = 1
 *   Single Aliasing: No
 *   Double Aliasing: No
 */
contract initializationd1n1 {
  
  constructor() {
  } 

  function initializationd1n1f(bool[1] memory x) 
    pure 
    external 
    returns (bool[1] memory)  
    {
        bool[1] memory y;
        y[0] = true;
        return x;
    }
}