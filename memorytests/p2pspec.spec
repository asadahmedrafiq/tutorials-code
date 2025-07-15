/**
 * # p2p Example
 *
 * This is the example of pointer to pointer assignment. Please check rule `p2passignspec`.
 * Run using:
 *
 * certoraRun ERC20.sol: --verify ERC20:ERC20Fixed.spec --solc solc8.0
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign2(uint8[5], uint8, uint8, uint8[5]) external returns (uint8[5] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array 
rule p2passignspec() {


    uint8[5] dest_array;
    uint8[5] ret;
    
    uint8[5] source_array;
    uint8 i;
    uint8 j;

    ret = assign2(e, dest_array,i, j, source_array);
    require i < 5;
    require j != i;
    require j<5;

   
/**@title return array contains the content of the source array
* 
*/
    assert ret[i] == source_array[j];

/**@title return array contains the content of the destination array
* 
*/
    assert ret[j] == dest_array[j];
}

