/**
 * 
 *
 * This is the example of value to pointer assignment for a 3D memory array with n=5. Please check rule `assign3spec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/test05.sol --verify test05:/home/asad/certora/tutorials-code/memorytests/assign3spec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign3(uint8[5][5][5], uint8, uint8, uint8, uint8) external returns (uint8[5][5][5] memory) envfree;
}

/// @title Assignment must change the data at specified index in destination array 
rule assign3spec() {


    uint8[5][5][5] dest_array3;
    uint8[5][5][5] ret3;
    
    uint8 i3;
    uint8 j3;
    uint8 k3;
    uint8 i31;
    uint8 j31;
    uint8 k31;
    uint8 value3;

    ret3 = assign3(dest_array3, i3, j3, k3, value3);
    
    require i3 < 5;
    require j3 < 5;    
    require k3 < 5;
    require i31 < 5;
    require j31 < 5;    
    require k31 < 5;
    require i3 != i31;
    require j3 != j31;
    require k3 != k31;
/**@title return array contains the content of the source array
* 
*/
    assert ret3 [i3][j3][k3] == value3;
    assert ret3 [i31][j31][k31] == dest_array3 [i31][j31][k31];
}

