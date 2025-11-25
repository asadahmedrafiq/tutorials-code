// SPDX-License-Identifier: GPL-3.0
// Test for initializing of memory array (initializationd2n1.sol). 
  /**Test configurations: 1
 *  #Dimensions (D) : D = 2
 *   Size       (n) : n = 1
 *   Single Aliasing: No
 *   Double Aliasing: No
 */
pragma solidity >=0.8.25;
 
contract initializationd2n1 {
    
  constructor() {
  } 
 
  function initializationd2n1f(bool[1][1] memory x) 
    pure 
    external 
    returns (bool[1][1] memory)  
    {
        bool[1][1] memory y;
        y[0][0] = true;
        return x;
    }
}