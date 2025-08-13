/**
 * # dynamicv2p Example
 *
 * This is the example of value to pointer assignment for a single dimenstional dynamic array. Please check rule `dassigndyvprule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test13.sol --verify test13:/home/asad/certora/tutorials-code/memorytests/assigndyvpspec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assigndyvp(uint8[], uint8, uint8) external returns (uint8[] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array with value
rule assigndyvprule() {


    uint8[] dest_array;
    uint8[] ret;
    
    uint8 value;
    uint8 i;
    uint8 j;
    require i !=j;
    require i < dest_array.size;
    require j < dest_array.size;

    ret = assigndyvp(dest_array, i, value);
   

/**@title return array contains the content of the source array
* 
*/
    assert ret[i] == value;

/**@title return array contains the content of the destination array
* 
*/
   assert ret[j] == dest_array[j];
}

