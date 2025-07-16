/**
 * # p2p Example
 *
 * This is the example of pointer to pointer assignment. Please check rule `dp2passignspec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/p2p.sol --verify p2p:/home/asad/certora/tutorials-code/memorytests/p2pspec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign2(uint8[], uint8, uint8, uint8[]) external returns (uint8[] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array 
rule dp2passignspec() {


    uint8[] dest_array;
    uint8[] ret;
    
    uint8[] source_array;
    uint8 i;
    uint8 j;

    ret = assign2(dest_array, i, j, source_array);
    require dest_array.length == source_array.length;
    require i < dest_array.length;
    require j != i;
    require j < source_array.length;

   
/**@title return array contains the content of the source array
* 
*/
    assert ret[i] == source_array[j];

/**@title return array contains the content of the destination array
* 
*/
    assert ret[j] == dest_array[j];
}

