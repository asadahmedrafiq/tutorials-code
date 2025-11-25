
/**
 * This is a specification file for singlealiasingd2n20.sol (singlealiasingd2n20spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/singlealiasingd2n20.sol --verify singlealiasingd2n20:/home/asad/certora/tutorials-code/memorytests/singlealiasingd2n20spec.spec
 *
 * There should be no errors.
 */
 
 /**Test results: 
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 *   loop complexity: High
 *            Result: Time out
 */
methods
{
    // Declare function as a method
    function singlealiasingd2n20f(uint8[20][20], uint8, uint8, uint8, uint8, uint8 [20][20]) external returns (uint8[20][20] memory) envfree;
  }

/// @title Assignment must change the data at specified index in destination array 
rule singlealiasingd2n20rule() {


    uint8[20][20] dest_array;
    uint8[20][20] ret;
    
    uint8[20][20] source_array;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 value;

    ret = singlealiasingd2n20f(dest_array, i, j, k, value, source_array);
    require i < 20;
    require j < 20;
    require k < 20;

   
/**@title return array contains the content of the source array
* 
*/
// Return/dest array contains values assigned to source array at specified index
    assert ret [i][k] == value;
}