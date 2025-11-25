
/**
 * This is the specification file for assignd2n20.sol (assignd2n20spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assignd2n20.sol --verify assignd2n20:/home/asad/certora/tutorials-code/memorytests/assignd2n20spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test resluts: 
 *        Path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 * loop complexity: High
 *            Result: Pass
 */
methods
{
    // Declared function as a method
    function assignd2n20f(uint8[20][20], uint8, uint8, uint8) external returns (uint8[20][20] memory) envfree;
  }

/// @title Assignment must change the data at specified index in destination array with value
rule assignd2n20rule() {


    uint8[20][20] dest_array;
    uint8[20][20] ret;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 value;
    require i < 5;
    require j < 5;
    require k < 5;

    ret = assignd2n20f(dest_array, i, j, value);
    
   
/**@title return array at specified index contains the content of the source array
* 
*/
    assert ret [i][j] == value;
}