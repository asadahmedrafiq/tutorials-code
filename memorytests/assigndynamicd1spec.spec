/**
 * This is specification file for assigndynamicd1.sol (assigndynamicd1spec.spec). 
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assigndynamicd1.sol --verify assigndynamicd1:/home/asad/certora/tutorials-code/memorytests/assigndynamicd1spec.spec --loop_iter 200
 *
 * There should be no errors.
 */
 
 /**Test Result: 
 *      path account: Low
 *      nonlinearity: Low
 *  memory complexity: Low
 *    Loop complexity: High
 *            Result: Pass
 */

methods
{
    // Declare function as a method
    function assigndynamicd1f(uint8[], uint8, uint8) external returns (uint8[] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array with value
rule assigndynamicd1rule() {


    uint8[] dest_array;
    uint8[] ret;
    
    uint8 value;
    uint8 i;
   // uint8 j;
    
// Ensure array has at least one element
    require dest_array.length > 0;
    // Limit size to avoid loop unwinding issues
    require dest_array.length < 5;
    // Ensure i is a valid index (strictly less than length)
    require i < dest_array.length;

    
    ret = assigndynamicd1f(dest_array, i, value);

    // Check the assigned value
    assert ret[i] == value;
}
