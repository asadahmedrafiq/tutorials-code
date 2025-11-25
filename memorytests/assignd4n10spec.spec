/**
 * 
 *
 * This is the specification file for assignd4n10.sol (assignd4n10spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assignd4n10.sol --verify assignd4n10:/home/asad/certora/tutorials-code/memorytests/assignd4n10spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test Result:
 *            Result: Problem
 */

methods
{
    // Declare function as a method
    function assignd4n10f(uint8[10][10][10][10], uint8, uint8, uint8, uint8, uint8) external returns (uint8[10][10][10][10] memory) envfree; 
}

/// @title Assignment must change the data at specified index in destination array 
rule assignd4n10rule() {


    uint8[10][10][10][10] dest_array;
    uint8[10][10][10][10] ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;

    require i < 10;
    require j < 10;    
    require k < 10;
    require l < 10;
    uint8 value;

    ret = assignd4n10f(dest_array, i, j, k, l, value);
    
    
/**@title return destination array contains the copied content of the source array at specified indeces
* 
*/
    assert ret [i][j][k][l] == value;
}


