
/**
 * This is a specification file for singlealiasingd2n5.sol (singlealiasingd2n5spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/singlealiasingd2n5.sol --verify singlealiasingd2n5:/home/asad/certora/tutorials-code/memorytests/singlealiasingd2n5spec.spec
 *
 * There should be no errors.
 */
 
  /**Test results:
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: medium
 *   loop complexity: High
 *            Result: pass
 */

methods
{
    // Declare function as a method
    function singlealiasingd2n5f(uint8[5][5], uint8, uint8, uint8, uint8, uint8 [5][5]) external returns (uint8[5][5] memory) envfree;
  }

/// @title Assignment must change the data at specified index in destination array 
rule singlealiasingd2n5rule() {


    uint8[5][5] dest_array;
    uint8[5][5] ret;
    
    uint8[5][5] source_array;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 value;

    ret = singlealiasingd2n5f(dest_array, i, j, k, value, source_array);
    require i < 5;
    require j < 5;
    require k < 5;
   
/**@title eturn/dest array contains values assigned to source array at specified index
* 
*/
    assert ret [i][k] == value;
}