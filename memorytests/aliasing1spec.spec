/**
 * # p2p Example
 *
 * This is the example of pointer to pointer assignment. Please check rule `aliasing1assignspec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/aliasing1.sol --verify p2p:/home/asad/certora/tutorials-code/memorytests/aliasing1pec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign3(uint8[50][50], uint8, uint8, uint8, uint8, uint8[50][50]) external returns (uint8[50][50] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array 
rule aliasing1assignspec() {


    uint8[50][50] dest_array;
    uint8[50][50] ret;
    
    uint8[50][50] source_array;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;
    uint8 m;
    uint8 n;
    uint8 value;

    ret = assign3(dest_array,i, j, k, value, source_array);
    require i < 50;
    require j < 50;
    require k < 50;
   require l < 50;
   require m < 50;
   require n < 50;
    require l != i;
    require n != k;

/**@title return array contains the content of the source array
* 
*/
    assert ret[i][k] == value;
    assert ret[l][m] == dest_array[l][m];
    assert ret[i][n] == source_array[j][n];
}