/**
 * # p2p Example
 *
 * This is the example of pointer to pointer assignment. Please check rule `daliasing1assignspec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test20.sol --verify test20:/home/asad/certora/tutorials-code/memorytests/daliasing1spec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function daliasing1(uint8[][], uint8, uint8, uint8, uint8, uint8[][]) external returns (uint8[][] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array 
rule daliasing1assignspec() {


    uint8[][] dest_array;
    uint8[][] ret;
    
    uint8[][] source_array;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 value;

    require dest_array.length > 0;
    require dest_array.length < 2;
    require source_array.length > 0;
    require source_array.length < 2;
    require i < source_array.length;
    require j < dest_array.length;
    require k > 0;
    require k < 2;

 
    ret = daliasing1(dest_array,i, j, k, value, source_array);
   
/**@title return array contains the content of the source array
* 
*/
    assert ret[i][k] == value;
}