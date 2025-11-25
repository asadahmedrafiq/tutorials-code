/**
 *
 * This is the specification file for assignd1n5.sol (assignd1n5spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assignd1n5.sol --verify assignd1n5:/home/asad/certora/tutorials-code/memorytests/assignd1n5spec.spec
 *
 * There should be no errors.
 */
 
 /**Test results:
 *        Path count: Low
 *      nonlinearity: Low
 * memory complexity: Low
 *   loop complexity: High
 *           Result: Pass
 */
 
methods
{
    // Decleartion of function as a method
    function assignd1n5f(uint8[5], uint8, uint8) external returns (uint8[5] memory) envfree;
  }


/// @title Assignment must change the data at specified index in destination array with value
rule assignd1n5frule() {


    uint8[5] dest_array;
    uint8[5] ret;
    
    uint8 value;
    uint8 i;
    uint8 j;
    require i < 5;

    ret = assignd1n5f(dest_array, i, value);
   
   
/**@title return array at specified index contains the content of the source array
* 
*/
    assert ret[i] == value;

}
