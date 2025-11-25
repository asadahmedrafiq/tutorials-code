
/**
 * This is the specification file for assignd2n5.sol (assignd2n5spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assignd2n5.sol --verify assignd2n5:/home/asad/certora/tutorials-code/memorytests/assignd2n5spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test result: 
 *        Path count: Low
 *      nonlinearity: Low
 * memory complexity: Medium
 * loop complexity: High
 *            Result: Pass
 */
methods
{
    // Declaring funciton as a method
    function assignd2n5f(uint8[5][5], uint8, uint8, uint8) external returns (uint8[5][5] memory) envfree;
  }

/// @title Assignment must change the data at specified index in destination array with value
rule assignd2n5rule() {


    uint8[5][5] dest_array;
    uint8[5][5] ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 value;
    require i < 5;
    require j < 5;
    require k < 5;

    ret = assignd2n5f(dest_array, i, j, value);
    
   
/**@title return array at specified index contains the content of the source array
* 
*/

    assert ret [i][j] == value;
}