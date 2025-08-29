/**
 * 
 * This is the example of pointer to pointer assignment with n=5. Please check rule `test26rule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test26.sol --verify test26:/home/asad/certora/tutorials-code/memorytests/test26spec.spec
 *
 * There should be no errors.
 */
 
 /**Test configurations: 
 *  Test behavior: dynamic memory array to dynamic memory array assignment followed by value assignment to source dynamic memroy array
 *  #Dimensions (D) : 1D
 *   Size       (n) : n = 5
 *   Single Aliasing: yes 
 *   Double Aliasing: No
 *            Result: 
 */
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function t26(uint8[], uint8, uint8, uint8, uint8[]) external returns (uint8[] memory) envfree;
}

/// @title Assignment must change the data at specified index in destination array 
rule test26rule() {


    uint8[] dest_array3;
    uint8[] ret3;
    
    uint8[] source_array3;
    uint8 i3;
    uint8 j3;
    uint8 value3;

    ret3 = t26(dest_array3, i3, j3, value3, source_array3);
    require i3 < 5;
    require j3 < 5;
    //x and y share i3 and j3 index in assignment operation. Therefore, 
    require j3 != i3;
    
   require dest_array3.length > 0;
   require source_array3.length > 0;
   require dest_array3.length < 5;
   require source_array3.length < 5;
   require source_array3.length == dest_array3.length;

   require i3 < dest_array3.length;
   require j3 < source_array3.length;
/**@title return array contains the content of the source array
* 
*/
//assert ret3 [j3] == value3; (Not valid)
    assert ret3 [i3] == source_array3 [j3];

/**@title return array contains the content of the destination array
* 
*/
    assert ret3 [j3] == dest_array3 [j3];
}

