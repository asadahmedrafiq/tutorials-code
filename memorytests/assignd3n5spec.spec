/**
 * This is the specification file for assignd3n5.sol (assignd3n5spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assignd3n5.sol --verify assignd3n5:/home/asad/certora/tutorials-code/memorytests/assignd3n5spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test results:
 *        Path count: Low
 *      nonlinearity: Low
 * memory complexity: Medium
 *   loop complexity: High
 *            Result: Time Out
 */
methods
{
    // Declared function as a method
    function assignd3n5f(uint8[5][5][5], uint8, uint8, uint8, uint8) external returns (uint8[5][5][5] memory) envfree;
}

/// @title Assignment must change the data at specified index in destination array 
rule assignd3n5rule() {


    uint8[5][5][5] dest_array;
    uint8[5][5][5] ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 i1;
    uint8 j1;
    uint8 k1;
    uint8 value;

    ret = assignd3n5f(dest_array, i, j, k, value);
    
    require i < 5;
    require j < 5;    
    require k < 5;
  
/**@title return array at specified index contains the content of the source array
* 
*/
    assert ret [i][j][k] == value;
}

