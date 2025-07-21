/**
 * # dynamicv2p Example
 *
 * This is the example of value to pointer assignment. Please check rule `dv2passignspec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/dynamicv2p.sol --verify p2p:/home/asad/certora/tutorials-code/memorytests/dynamicv2pspec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign2(uint8[], uint8, uint8) external returns (uint8[] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array with value
rule dv2passignspec() {


    uint8[] dest_array;
    uint8[] ret;
    
    uint8 value;
    uint8 i;
    
    ret = assign2(dest_array, i, value);
    require dest_array.length < 5;
     require i < dest_array.length;

/**@title return array contains the content of the source array
* 
*/
    assert ret[i] == value;

/**@title return array contains the content of the destination array
* 
*/
    assert ret[i] == dest_array[i];
}

