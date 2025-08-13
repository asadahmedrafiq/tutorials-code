/**
 * # dynamicv2p Example
 *
 * This is the example of value to pointer assignment for a single dimenstional dynamic array. Please check rule `dassigndy2dptprule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test14.sol --verify test14:/home/asad/certora/tutorials-code/memorytests/assigndy2sdptpspec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
 function assigndy2dptp(uint8[][], uint8, uint8, uint8, uint8 uint8[][]) external returns (uint8[] memory) envfree;
}

/// @title Assignment must change the data at specified index in destination array 
rule aliasing1assignspec() {


    uint8[][] dest_array;
    uint8[][] ret;
    
    uint8[][] source_array;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;
    uint8 m;
    uint8 n;
    uint8 value;

    ret = assigndy2dptp(dest_array,i, j, k, value, source_array);
    require i < dest_array.length;
    require j < dest_array.length;
    require k < source_array.length;
   require l < source_array.length;
 
/**@title return array contains the content of the source array
* 
*/
    assert ret[i][k] == value;
    assert ret[l][m] == dest_array[l][m];
    assert ret[i][n] == source_array[j][n];
}