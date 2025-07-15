/**
 * # p2p Example
 *
 * This is the example of pointer to pointer assignment. Please check rule `aliasing1assignspec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/aliasing1.sol --verify p2p:/home/asad/certora/tutorials-code/memorytests/aliasing1pec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign3(uint8[5][5], uint8, uint8, uint8, uint8, uint8[5][5]) external returns (uint8[5][5] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array 
rule aliasing1assignspec() {


    uint8[5][5] dest_array;
    uint8[5][5] ret;
    
    uint8[5][5] source_array;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 value;

    ret = assign3(dest_array,i, j, k, value, source_array);
    require i < 5;
    require j < 5;
    require k < 5;
   
/**@title return array contains the content of the source array
* 
*/
    assert ret[i][k] == value;
}