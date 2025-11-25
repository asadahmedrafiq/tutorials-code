/**
* This is a specification file for singlealiasingd4n5.sol (singlealiasingd4n5spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/singlealiasingd4n5.sol --verify singlealiasingd4n5:/home/asad/certora/tutorials-code/memorytests/singlealiasingd4n5spec.spec 
 *
 * There should be no errors.
 */
 

 /**Test results: 
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 *   loop complexity: High
 *            Result: Problem
 *Out of Resources
 *Extremely low available memory: 61MB out of a total of 35000MB are left. The prover likely crashes soon and results will be incomplete.
 *
 */

methods
{
    // Declare function as a method
    function singlealiasingd4n5f (uint8[5][5][5][5], uint8, uint8, uint8, uint8, uint8, uint8, uint8 [5][5][5][5]) external returns (uint8[5][5][5][5] memory) envfree; 
 }

/// @title Assignment must change the data at specified index in destination array 
rule singlealiasingd4n5rule() {


    uint8[5][5][5][5] dest_array;
    uint8[5][5][5][5] source_array;
    uint8[5][5][5][5] ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;
    uint8 m;

    uint8 value;

    ret = singlealiasingd4n5f(dest_array, i, j, k, l, m, value, source_array);
    
    require i < 5;
    require j < 5;    
    require k < 5;
    require l < 5;
    require m < 5;
    
/**@title return destination array contains the copied content of the source array at specified indeces
* 
*/
    assert ret [i][k][l][m] == value;
}