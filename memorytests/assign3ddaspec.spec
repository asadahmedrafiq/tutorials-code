
/**
 * # v2p Example
 *
 * This is the example of value to pointer assignment. Please check rule `assign3ddarule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test11.sol --verify test11:/home/asad/certora/tutorials-code/memorytests/assign3ddaspec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign3dda(uint8[5][5][5], uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8[5][5][5], uint8[5][5][5]) 
             external 
             returns (uint8[5][5][5] memory) 
             envfree; 
 
  }

/// @title Assignment must change the data at specified index in destination array 
rule assign3ddarule() {


    uint8[5][5][5] dest_array3;
    uint8[5][5][5] ret3;
    uint8[5][5][5] t_array3;
    uint8[5][5][5] source_array3;

    uint8 i3;
    uint8 j3;
    uint8 k3;
    uint8 l3;
    uint8 m3;
    uint8 n3;
    uint8 value3;

    ret3 = assign3dda(dest_array3, i3, j3, k3, l3, m3, n3, value3, source_array3, t_array3);
    require i3 < 5;
    require j3 < 5;
    require k3 < 5;
    require l3 < 5;
    require m3 < 5;
    require n3 < 5;

   
/**@title return array contains the content of the destination array
* 
*/
// Return/dest array contains values assigned to destination array at specified index
    assert ret3 [i3][k3][n3] == value3;
}