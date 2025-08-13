
/**
 * # v2p Example
 *
 * This is the example of value to pointer assignment. Please check rule `assign2dp2pspec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test09.sol --verify test09:/home/asad/certora/tutorials-code/memorytests/assign2dp2pspec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign2dp2p(uint8[5][5], uint8, uint8, uint8, uint8, uint8 [5][5]) external returns (uint8[5][5] memory) envfree;
  }

/// @title Assignment must change the data at specified index in destination array 
rule assign2dp2prule() {


    uint8[5][5] dest_array3;
    uint8[5][5] ret3;
    
    uint8[5][5] source_array3;
    uint8 i3;
    uint8 j3;
    uint8 k3;
    uint8 value3;

    ret3 = assign2dp2p(dest_array3, i3, j3, k3, value3, source_array3);
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