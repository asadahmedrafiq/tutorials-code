/**
 * This is a specification file for singlealiasingd3n5.sol (singlealiasingd3n5spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/singlealiasingd3n5.sol --verify singlealiasingd3n5:/home/asad/certora/tutorials-code/memorytests/singlealiasingd3n5spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test results: 
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 *   loop complexity: High
 *           Result: Pass
 */

methods
{
    // Declared function as a method
    function singlealiasingd3n5f(uint8[5][5][5], uint8, uint8, uint8, uint8, uint8, uint8[5][5][5]) external returns (uint8[5][5][5] memory) envfree; 
}

/// @title Assignment must change the data at specified index in destination array 
rule singlealiasingd3n5rule() {


    uint8[5][5][5] dest_array;
    uint8[5][5][5] source_array;
    uint8[5][5][5] ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;

    uint8 value;

    ret = singlealiasingd3n5f(dest_array, i, j, k, l, value, source_array);
    
    require i < 5;
    require j < 5;    
    require k < 5;
    require l < 5;
   

/**@title return destination array contains the copied content of the source array at specified indeces
* 
*/
    assert ret [i][k][l] == value;
}

