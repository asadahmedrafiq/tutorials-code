
/**
 * This is specification file for double aliasing for doublealiasingd4n10.sol(doublealiasingd4n5spec.spec). 
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/doublealiasingd4n10.sol --verify doublealiasingd4n10:/home/asad/certora/tutorials-code/memorytests/doublealiasingd4n10spec.spec
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
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function doublealiasingd4n10f(uint8[10][10][10][10], uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8[10][10][10][10], uint8[10][10][10][10]) 
             external 
             returns (uint8[10][10][10][10] memory) 
             envfree; 
 
  }

/// @title Assignment must change the data at specified index in destination array 
rule doublealiasingd4n10rule() {


    uint8[10][10][10][10] dest_array;
    uint8[10][10][10][10] ret;
    uint8[10][10][10][10] t_array;
    uint8[10][10][10][10] source_array;

    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;
    uint8 m;
    uint8 n;
    uint8 o;
    uint8 value;

    ret = doublealiasingd4n10f(dest_array, i, j, k, l, m, n, o, value, source_array, t_array);

    require i < 10;
    require j < 10;
    require k < 10;
    require l < 10;
    require m < 10;
    require n < 10;
    require o < 10;
       
/**@title return array contains the content of the destination array
* 
*/
// Return/dest array contains values assigned to destination array at specified index
    assert ret [i][k][n][o] == value;
}