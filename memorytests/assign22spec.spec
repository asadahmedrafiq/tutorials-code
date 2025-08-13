/**
 * # p2p Example
 *
 * This is the example of pointer to pointer assignment with n=20. Please check rule `assign22spec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test04.sol --verify test04:/home/asad/certora/tutorials-code/memorytests/assign22spec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign22(uint8[20], uint8, uint8, uint8, uint8[20]) external returns (uint8[20] memory) envfree;
 
}

/// @title Assignment must change the data at specified index in destination array 
rule assign22spec() {


    uint8[20] dest_array3;
    uint8[20] ret3;
    
    uint8[20] source_array3;
    uint8 i3;
    uint8 j3;
    uint8 value3;

    ret3 = assign22(dest_array3, i3, j3, value3, source_array3);
    require i3 < 20;
    require j3 < 20;
    require j3 != i3;
    
   
/**@title return array contains the content of the source array
* 
*/
    assert ret3 [i3] == source_array3 [j3];

/**@title return array contains the content of the destination array
* 
*/
    assert ret3 [j3] == dest_array3 [j3];
}

