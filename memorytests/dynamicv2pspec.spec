/**
 * # dynamicv2p Example
 *
 * This is the example of value to pointer assignment. Please check rule `dv2passignspec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test17.sol --verify test17:/home/asad/certora/tutorials-code/memorytests/dynamicv2pspec.spec
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
   // uint8 j;
    
// Ensure array has at least one element
    require dest_array.length > 0;
    // Limit size to avoid loop unwinding issues
    require dest_array.length < 2;
    // Ensure i is a valid index (strictly less than length)
    require i < dest_array.length;

    
    ret = assign2(dest_array, i, value);

    // Check the assigned value
    assert ret[i] == value;
}

