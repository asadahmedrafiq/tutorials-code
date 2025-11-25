/**
 * 
 * This is the specification file for assignd3n10.sol (assignd3n10spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assignd3n10.sol --verify assignd3n10:/home/asad/certora/tutorials-code/memorytests/assignd3n10spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test results:
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 *   loop complexity: High
 *          Result  : Time out
 */
methods
{
    // Declared function as a method
    function assignd3n10f(uint8[10][10][10], uint8, uint8, uint8, uint8) external returns (uint8[10][10][10] memory) envfree;
}

/// @title Assignment must change the data at specified index in destination array 
rule assignd3n10rule() {


    uint8[10][10][10] dest_array;
    uint8[10][10][10] ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 i1;
    uint8 j1;
    uint8 k1;
    uint8 value;

    ret = assignd3n10f(dest_array, i, j, k, value);
    
    require i < 10;
    require j < 10;    
    require k < 10;
  
/**@title return array contains the content of the source array
* 
*/
    assert ret [i][j][k] == value;
}

