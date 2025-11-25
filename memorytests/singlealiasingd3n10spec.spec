/**
 * 
 *
 * This is a specification file for singlealiasingd3n10.sol (singlealiasingd3n10spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/singlealiasingd3n10.sol --verify singlealiasingd3n10:/home/asad/certora/tutorials-code/memorytests/singlealiasingd3n10spec.spec
 *
 * There should be no errors.
 */
 
 
 /**Test results: 
 *        path count: Low
 *      nonlinearity: Low
 * memory complexity: High
 *   loop complexity: High
 *            Result: Problem
 /* Global notification:
 Out of Resources

Extremely low available memory: 0MB out of a total of 35000MB are left. The prover likely crashes soon and results will be incomplete.

Out of Resources

Extremely low available memory: 0MB out of a total of 35000MB are left. The prover likely crashes soon and results will be incomplete.

Out of Resources

Extremely low available memory: 112MB out of a total of 35000MB are left. The prover likely crashes soon and results will be incomplete.

Out of Resources

Extremely low available memory: 3MB out of a total of 35000MB are left. The prover likely crashes soon and results will be incomplete.

Out of Resources

Extremely low available memory: 48MB out of a total of 35000MB are left. The prover likely crashes soon and results will be incomplete.

Out of Resources

Extremely low available memory: 62MB out of a total of 35000MB are left. The prover likely crashes soon and results will be incomplete.

Out of Resources

Extremely low available memory: 62MB out of a total of 35000MB are left. The prover likely crashes soon and results will be incomplete.
 */      
 */

methods
{
    // Declare fucntion as a method
    function singlealiasingd3n10f(uint8[10][10][10] , uint8, uint8, uint8, uint8, uint8, uint8[10][10][10])  external returns (uint8[10][10][10]  memory) envfree; 
}

/// @title Assignment must change the data at specified index in destination array 
rule singlealiasingd3n10rule() {


    uint8[10][10][10]  dest_array;
    uint8[10][10][10]  source_array;
    uint8[10][10][10]  ret;
    
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;

    uint8 value;

    ret = singlealiasingd3n10f(dest_array, i, j, k, l, value, source_array);
    
    require i < 10;
    require j < 10;    
    require k < 10;
    require l < 10;

/**@title return destination array contains the copied content of the source array at specified indeces
* 
*/
    assert ret [i][k][l] == value;
}

