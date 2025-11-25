/**
 * This is the specification file for assignd4n5.sol (assignd4n5spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assignd4n5.sol --verify assignd4n5:/home/asad/certora/tutorials-code/memorytests/assignd4n5spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test results: 
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 *   loop complexity: High
  *           Result: Time out
 */

methods
{
    // Declare function as a method
    function assignd4n5f(uint8[5][5][5][5], uint8, uint8, uint8, uint8, uint8) external returns (uint8[5][5][5][5] memory) envfree; 
}

/// @title Assignment must change the data at specified index in destination array 
rule assignd4n5rule() {


    uint8[5][5][5][5] dest_array;
    uint8[5][5][5][5] ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;

    uint8 value;
    require i < 5;
    require j < 5;    
    require k < 5;
    require l < 5;

    ret = assignd4n5f(dest_array, i, j, k, l, value);
    

/**@title return array at specified index contains the content of the source array
* 
*/
    assert ret [i][j][k][l] == value;

}


