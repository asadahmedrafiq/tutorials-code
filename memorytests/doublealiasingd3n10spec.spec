
/**
 * This is specification file for double aliasing for doublealiasingd3n10.sol(doublealiasingd3n10spec.spec). 
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/doublealiasingd3n10.sol --verify doublealiasingd3n10:/home/asad/certora/tutorials-code/memorytests/doublealiasingd3n10spec.spec
 *
 * There should be no errors.
 */
 
 /**Test Result:
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 *   loop complexity: High
 *            Result: Killed

 */

methods
{
    // Declare funciton as a method
    function doublealiasingd3n10f(uint8[10][10][10], uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8[10][10][10], uint8[10][10][10]) 
             external 
             returns (uint8[10][10][10] memory) 
             envfree; 
 
  }

/// @title Assignment must change the data at specified index in destination array 
rule doublealiasingd3n10rule() {


    uint8[10][10][10] dest_array;
    uint8[10][10][10] ret;
    uint8[10][10][10] t_array;
    uint8[10][10][10] source_array;

    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;
    uint8 m;
    uint8 n;
    uint8 value;

    ret = doublealiasingd3n10f(dest_array, i, j, k, l, m, n, value, source_array, t_array);
    require i < 10;
    require j < 10;
    require k < 10;
    require l < 10;
    require m < 10;
    require n < 10;
   
/**@title return array contains the content of the destination array
* 
*/
// Return/destination array contains values assigned to destination array at specified index
    assert ret [i][k][n] == value;
   }