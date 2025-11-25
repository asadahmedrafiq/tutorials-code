/**
 * This is the specification file for assignd1n20.sol (assignd1n20spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/assignd1n20.sol --verify assignd1n20:/home/asad/certora/tutorials-code/memorytests/assignd1n20spec.spec
 *
 * There should be no errors.
 */
 
  
 /**Test Reslut:
 *        Path count: Low
 *      nonlinearity: Low
 * memory complexity: Medium
 *   loop complexity: High
 *            Result: Pass
 */
methods
{
// Declaration of function as a method
    function assignd1n20f(uint8[20], uint8, uint8) external returns (uint8[20] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array with value.
rule assignd1n20rule() {


    uint8[20] dest_array;
    uint8[20] ret;
    
    uint8 value;
    uint8 i;
    uint8 j;

    ret = assignd1n20f(dest_array, i, value);
    require i < 20;
   
/**@title return array containing the content of the source array
* 
*/
    assert ret[i] == value;

}
