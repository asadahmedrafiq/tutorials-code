/**
 * 
 * This is the example of pointer to pointer assignment with n=5. Please check rule `test27rule`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test28.sol --verify test28:/home/asad/certora/tutorials-code/memorytests/test28spec.spec
 *
 * There should be no errors.
 */
 
 /**Test configurations: 
 *  Test behavior: Double aliasing for single dimension, small size static memory aray
 *  #Dimensions (D) : 1D
 *   Size       (n) : n = 20
 *   Single Aliasing: No 
 *   Double Aliasing: yes
 *            Result: pass
 */
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function t28(uint8[20], uint8, uint8, uint8, uint8, uint8[20], uint8[20]) external returns (uint8[20] memory) envfree;
}

/// @title Assignment in case of intermediatary memory array
rule test28rule() {


    uint8[20] dest_array3;
    uint8[20] ret3;
    
    uint8[20] source_array3;
    uint8[20] transient_array3;

    uint8 i3;
    uint8 j3;
    uint8 k3;
    uint8 value3;

    ret3 = t28(dest_array3, i3, j3, k3, value3, source_array3, transient_array3);
    require i3 < 20;
    require j3 < 20;
    require k3 < 20;
   
   
/**@title return array contains the content of the transent array
* 
*/
    assert ret3 [i3] == transient_array3 [j3];

}

