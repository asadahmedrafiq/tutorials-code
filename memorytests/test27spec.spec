/**
 * 
 * This is the example of pointer to pointer assignment with n=5. Please check rule `test27rule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test27.sol --verify test27:/home/asad/certora/tutorials-code/memorytests/test27spec.spec
 *
 * There should be no errors.
 */
 
 /**Test configurations: 
 *  Test behavior: Double aliasing for single dimension, small size static memory aray
 *  #Dimensions (D) : 1D
 *   Size       (n) : n = 5
 *   Single Aliasing: No 
 *   Double Aliasing: yes
 *            Result: pass
 */
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function t27(uint8[5], uint8, uint8, uint8, uint8, uint8[5], uint8[5]) external returns (uint8[5] memory) envfree;
}

/// @title Assignment in case of intermediatary memory array
rule test27rule() {


    uint8[5] dest_array3;
    uint8[5] ret3;
    
    uint8[5] source_array3;
    uint8[5] transient_array3;

    uint8 i3;
    uint8 j3;
    uint8 k3;
    uint8 value3;

    ret3 = t27(dest_array3, i3, j3, k3, value3, source_array3, transient_array3);
    require i3 < 5;
    require j3 < 5;
    require k3 < 5;
   
   
/**@title return array contains the content of the transent array
* 
*/
    assert ret3 [i3] == transient_array3 [j3];

}

