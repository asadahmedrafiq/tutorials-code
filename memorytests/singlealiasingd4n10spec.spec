/**
* This is a specification file for singlealiasingd4n10.sol (singlealiasingd4n10spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/singlealiasingd4n10.sol --verify singlealiasingd4n10:/home/asad/certora/tutorials-code/memorytests/singlealiasingd4n10spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test results:
 *        path count: Not applicable
 *      nonlinearity: Not applicable
 * memory complexity: Not applicable
 *   loop complexity: Not applicable
 *            Result: Problem
 */

methods
{
    // Declare function as a method
    function singlealiasingd4n10f (uint8[10][10][10][10] , uint8, uint8, uint8, uint8, uint8, uint8, uint8[10][10][10][10])  external returns (uint8[10][10][10][10]  memory) envfree; 
}

/// @title Assignment must change the data at specified index in destination array 
rule singlealiasingd4n10rule() {


    uint8[10][10][10][10]  dest_array;
    uint8[10][10][10][10]  source_array;
    uint8[10][10][10][10]  ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;
    uint8 m;

    uint8 value;

    ret = singlealiasingd4n10f (dest_array, i, j, k, l, m, value, source_array);
    
    require i < 10;
    require j < 10;    
    require k < 10;
    require l < 10;
    require m < 10;

/**@title return destination array contains the copied content of the source array at specified indeces
* 
*/
    assert ret [i][k][l][m] == value;
}

