/**
 * # dynamicaliasing2 Example
 *
 * This is the example of aliasing assignment involving three-dimensional arrays. Please check rule `daliasing2assignspec`.
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/aliasing2.sol --verify p2p:/home/asad/certora/tutorials-code/memorytests/aliasing2pec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
function assign4(uint8[][][], uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8[][][], uint8[][][]) external returns (uint8[][][] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array 
rule daliasing1assignspec() {


    uint8[][][] dest_array;
    uint8[][][] ret;
    
    uint8[][][] transient_array;
    uint8[][][] source_array;
    uint8 i;
    uint8 j;
    uint8 k;
    uint8 l;
    uint8 m;
    uint8 n;

    uint8 value;

    ret = assign4(dest_array, i, j, k, l, m, n, value, transient_array, source_array);
    require i < dest_array.length;
    require j < dest_array.length;
    require k < transient_array.length;
    require l < transient_array.length;
    require m < source_array.length;
    require n < source_array.length;
   
/**@title return array contains the content of the source array
* 
*/
   assert ret[i][k][n] == value;
}