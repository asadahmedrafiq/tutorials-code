/**
 * 
 * This is the example of pointer to pointer assignment with n=5. Please check rule `test03rule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test03.sol --verify test03:/home/asad/certora/tutorials-code/memorytests/test03spec.spec
 *
 * There should be no errors.
 */
 
 /**Test configurations: 
 *  Test behavior: memory array to memory array assignment followed by value assignment to source memroy array
 *  #Dimensions (D) : 1D
 *   Size       (n) : n = 5
 *   Single Aliasing: No 
 *   Double Aliasing: No
 *            Result: pass
 */
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function t03(uint8[5], uint8, uint8, uint8, uint8[5]) external returns (uint8[5] memory) envfree;
}

/// @title Assignment must change the data at specified index in destination array 
rule test03rule() {


    uint8[5] dest_array3;
    uint8[5] ret3;
    
    uint8[5] source_array3;
    uint8 i3;
    uint8 j3;
    uint8 value3;

    ret3 = t03(dest_array3, i3, j3, value3, source_array3);
    require i3 < 5;
    require j3 < 5;
    //x and y share i3 and j3 index in assignment operation. Therefore, 
    require j3 != i3;
    
   
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

