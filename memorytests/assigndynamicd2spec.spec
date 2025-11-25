
/**
* This is the specification file for assigndynamicd2.sol (assigndynamicd2spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assigndynamicd2.sol --verify assigndynamicd2:/home/asad/certora/tutorials-code/memorytests/assigndynamicd2spec.spec --loop_iter 200
 *
 * There should be no errors.
 */
 
 
 /**Test Result:
 *            Result: Problem
 */
methods
{
    // Function is declared as a method
    function assigndynamicd2f(uint8[][], uint8, uint8, uint8) external returns (uint8[][] memory) envfree;
  }

/// @title Assignment must change the data at specified index in destination array 
rule assigndynamicd2rule() {


    uint8[][] dest_array;
    uint8[][] ret;
    
    uint8 i;
    uint8 j;
    uint8 value;
    
   require dest_array.length > 0;
   require i < dest_array.length;
   require j < dest_array[i].length;
   require dest_array.length < 5;
   require dest_array[i].length < 5;

    ret = assigndynamicd2f(dest_array, i, j, value);
   

   
/**@title Return/dest array contains values assigned to source array at specified index
* 
*/
    assert ret [i][j] == value;

}