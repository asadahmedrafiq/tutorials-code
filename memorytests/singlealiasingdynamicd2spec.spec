/**
* This is a specification file for singlealiasingdynamicd2.sol (singlealiasingdynamicd2spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/singlealiasingdynamicd2.sol --verify singlealiasingdynamicd2:/home/asad/certora/tutorials-code/memorytests/singlealiasingdynamicd2spec.spec --loop_iter 200
 *
 * There should be no errors.
 */
 
 /**Test results: 
 *            Result: Problem
 */

methods
{
    // Declaring function as a method
 function singlealiasingdynamicd2f(uint8[][], uint8, uint8, uint8, uint8, uint8[][]) external returns (uint8[][] memory) envfree;
}

/// @title Assignment must change the data at specified index in destination array 
rule singlealiasingdynamicd2rule() {


    uint8[][] dest_array;
    uint8[][] ret;
    
    uint8[][] source_array;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 value;


    require dest_array.length   > 0;
    require source_array.length > 0;
    require dest_array.length   < 5;
    require source_array.length < 5;
    require i < dest_array.length;
    require j < dest_array.length;
    require k < source_array.length;

    ret = singlealiasingdynamicd2f(dest_array,i, j, k, value, source_array);

 
/**@title return array contains the content of the source array
* 
*/
    assert ret[i][k] == value;
}