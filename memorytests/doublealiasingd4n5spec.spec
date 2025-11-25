
/**
 * This is specification file for double aliasing for doublealiasingd4n5.sol (doublealiasingd4n5spec.spec). 
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/doublealiasingd4n5.sol --verify doublealiasingd4n5:/home/asad/certora/tutorials-code/memorytests/doublealiasingd4n5spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test results: 
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 *   loop complexity: High
 *            Result: Problem

 */

methods
{
    // Declare function as a method
    function doublealiasingd4n5f(uint8[5][5][5][5], uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8[5][5][5][5], uint8[5][5][5][5]) 
             external 
             returns (uint8[5][5][5][5] memory) 
             envfree; 
 
  }

/// @title Assignment must change the data at specified index in destination array 
rule doublealiasingd4n5rule() {


    uint8[5][5][5][5] dest_array;
    uint8[5][5][5][5] ret;
    uint8[5][5][5][5] t_array;
    uint8[5][5][5][5] source_array;

    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;
    uint8 m;
    uint8 n;
    uint8 o;
    uint8 value;

    ret = doublealiasingd4n5f(dest_array, i, j, k, l, m, n, o, value, source_array, t_array);
    require i < 5;
    require j < 5;
    require k < 5;
    require l < 5;
    require m < 5;
    require n < 5;
    require o < 5;

/**@title return array contains the content of the destination array
* 
*/
// Return/dest array contains values assigned to destination array at specified index
    assert ret [i][k][n][o] == value;
}