
/**
 * This is the example of value to pointer assignment. Please check rule `test16rule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test16.sol --verify test16:/home/asad/certora/tutorials-code/memorytests/test16spec.spec
 *
 * There should be no errors.
 */
 

 /**Test configurations: 
 *  Test behavior: Double aliasing with 2D static memory array  
 *  #Dimensions (D) : 2D
 *   Size       (n) : n = 5
 *   Single Aliasing: No
 *   Double Aliasing: Yes
 * Dynamic (n bound): NA
 *            Result: TBD
 *         iter_loop:
 */

methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
  function t16(uint8[2][2], uint8, uint8, uint8,  uint8, uint8, uint8[2][2], uint8[2][2]) external returns (uint8 [2][2] memory) envfree; 
  }

/// @title Assignment must change the data at specified index in destination array 
rule test16rule() {


    uint8[2][2] dest_array3;
    uint8[2][2] ret3;
    
    uint8[2][2] source_array3;
    uint8[2][2] transient_array;
    uint8 i3;
    uint8 j3;
    uint8 k3;
    uint8 l3;
    uint8 m;
    uint8 value3;

    require i3 < 2;
    require j3 < 2;
    require k3 < 2;
    require l3 < 2;

    ret3 = t16(dest_array3, i3, j3, k3, l3, value3, source_array3, transient_array);

    //require j3 != i3;
    
   
/**@title return array contains the content of the source array
* 
*/
// Return/dest array does not contain values assigned to source array at specified index
    assert ret3 [j3][l3] == source_array3[k3][l3];
// Retrun/dest array comparison for all other values which do not lie on the value3 index

//    assert ret3 [j3][k3] == dest_array3[j3][k3];
}