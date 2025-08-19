
/**
 * # v2p Example
 *
 * This is the example of value to pointer assignment. Please check rule `test15rule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test15.sol --verify test15:/home/asad/certora/tutorials-code/memorytests/test15spec.spec
 *
 * There should be no errors.
 */
 

 /**Test configurations: 
 *  Test behavior: Single aliasing with 2D static memory array  
 *  #Dimensions (D) : 2D
 *   Size       (n) : n = 50
 *   Single Aliasing: Yes
 *   Double Aliasing: No
 * Dynamic (n bound): NA
 *            Result: error
 *test15rule expanded to too many commands: 3343478 > 1000000. You can configure maxCommandCount accordingly
 */

methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function t15(uint8[50][50], uint8, uint8, uint8, uint8, uint8 [50][50]) external returns (uint8[50][50] memory) envfree;
  }

/// @title Assignment must change the data at specified index in destination array 
rule test15rule() {


    uint8[50][50] dest_array3;
    uint8[50][50] ret3;
    
    uint8[50][50] source_array3;
    uint8 i3;
    uint8 j3;
    uint8 k3;
    uint8 value3;

    ret3 = t15(dest_array3, i3, j3, k3, value3, source_array3);
    require i3 < 5;
    require j3 < 5;
    require k3 < 5;

    require j3 != i3;
    
   
/**@title return array contains the content of the source array
* 
*/
// Return/dest array contains values assigned to source array at specified index
    assert ret3 [i3][k3] == value3;
// Retrun/dest array comparison for all other values which do not lie on the value3 index

    assert ret3 [j3][k3] == dest_array3[j3][k3];
}