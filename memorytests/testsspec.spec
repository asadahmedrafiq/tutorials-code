/**
 * # Memory assignment tests specification in Certora.
 *
 * This file contains rules in Certora for the memroy arrays assignments in Solidity: 
 * assign1spec, 
 * assign2spec, 
 * assign3spec, 
 * assign4spec, 
 * assign5spec, 
 * assign6spec, 
 * assign7spec, 
 * assign8spec    
 *
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/tests.sol --verify tests:/home/asad/certora/tutorials-code/memorytests/testsspec.spec
 *
 * There should be no errors.
 */
 
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function assign1(uint8[5], uint8, uint8) external returns (uint8[5] memory) envfree;
    function assign2(uint8[50], uint8, uint8) external returns (uint8[50] memory) envfree;
    function assign3(uint8[5][5], uint8, uint8, uint8, uint8, uint8[5][5]) external returns (unit8[5][5] memory) envfree; 
    function assign4(uint8[50][50], uint8, uint8, uint8, uint8, uint8[50][50]) external returns (unit8[50][50] memory) envfree; 
    function assign5(uint8[5][5][5], uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8[5][5][5], uint8[5][5][5] ) external returns (uint8[5][5][5] memory) envfree;
    function assign6(uint8[50][50][50], uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8[50][50][50], uint8[50][50][50] ) external returns (uint8[50][50][50] memory) envfree;
    function assign7(uint8[], uint8 i, uint8 y) external returns (uint8[] memory) envfree;
    function assign8(uint8[][], uint8 i, uint8 y) external returns (uint8[][] memory) envfree;
}


/// @title Assignment must change the data at specified index in destination array with value
rule assign1spec() {


    uint8[5] dest_array1;
    uint8[5] ret1;
    
    uint8 value1;
    uint8 i1;
    uint8 j1;

    ret1 = assign1(dest_array1, i1, value1);
    require i1 < 5;
    require i1 != j1;
    require j1 < 5;
   
/**@title return array contains the content of the source array
* 
*/
    assert ret1 [i1] == value1;

/**@title return array contains the content of the destination array
* 
*/
    assert ret1 [j1] == dest_array1 [j1];
}

/// @title Assignment must change the data at specified index in destination array with value
rule assign2spec() {


    uint8[50] dest_array2;
    uint8[50] ret2;
    
    uint8 value2;
    uint8 i2;
    uint8 j2;

    ret = assign2(dest_array2, i2, value2);
    require i2 < 50;
    require i2 != j2;
    require j2 < 50;
   
/**@title return array contains the content of the source array
* 
*/
    assert ret2 [i2] == value2;

/**@title return array contains the content of the destination array
* 
*/
    assert ret2 [j2] == dest_array2 [j2];
}

/// @title Assignment must change the data at specified index in destination array 
rule assign3spec() {


    uint8[5] dest_array3;
    uint8[5] ret3;
    
    uint8[5] source_array3;
    uint8 i3;
    uint8 j3;

    ret = assign2(dest_array3, i3, j3, source_array3);
    require i3 < 5;
    require j3 != i3;
    require j3 < 5;

   
/**@title return array contains the content of the source array
* 
*/
    assert ret3 [i3] == source_array3 [j3];

/**@title return array contains the content of the destination array
* 
*/
    assert ret3 [j3] == dest_array3 [j3];
}

/// @title Pointer to pointer assignment must change the data at specified index in 2D destination array after update are the corresponding index 
rule assign4spec() {


    uint8[5] dest_array4;
    uint8[5] ret4;
    
    uint8[5] source_array4;
    uint8 i4;
    uint8 j4;

    ret4 = assign4(dest_array4,i4, j4, source_array4);
    require i4 < 5;
    require j4 != i4;
    require j4 < 5;

   
/**@title return array contains the content of the source array
* 
*/
    assert ret4 [i4] == source_array4 [j4];

/**@title return array contains the content of the destination array
* 
*/
    assert ret4 [j4] == dest_array4 [j4];
}


/// @title Aliasing using 3D memory arrays 
rule assign5spec() {


    uint8[5][5][5] dest_array5;
    uint8[5][5][5] ret5;
    
    uint8[5][5][5] transient_array5;
    uint8[5][5][5] source_array5;
    uint8 i5;
    uint8 j5;
    uint8 k5;
    uint8 l5;
    uint8 m5;
    uint8 n5;
    uint8 n51;
    uint8 n52;
    uint8 i51;
    uint8 k51;
    uint8 k52;

    uint8 value5;

    ret = assign5(dest_array5,i5, j5, k5, l5, m5, n5, value5, transient_array5, source_array5);
    require i5 < 5;
    require j5 < 5;
    require k5 < 5;
    require l5 < 5;
    require m5 < 5;
    require n5 < 5;
    require i51 < 5;
    require i51 != i5;
    require k51 < 5;
    require n51 < 5;
    require k52 < 5;
    require k52 != k5;
    require n52 < 5;
    require n52 != n5;

   
/**@title return array contains the content of the source array
* 
*/
   assert ret5 [i5][k5][n5] == value5;
   assert ret5 [i51][k51][n51] == dest_array5 [i51][k51][n51];
   assert ret5 [i5][k52][n51] == transient_array5 [j5][k5][n51];
   assert ret5 [i5][k5][n52] == source_array5 [l5][m5][n52];
}


/// @title Aliasing using 3D memory arrays 
rule assign6spec() {


    uint8[50][50][50] dest_array6;
    uint8[50][50][50] ret6;
    
    uint8[50][50][50] transient_array6;
    uint8[50][50][50] source_array6;
    uint8 i6;
    uint8 j6;
    uint8 k6;
    uint8 l6;
    uint8 m6;
    uint8 n6;
    uint8 n61;
    uint8 n62;
    uint8 i61;
    uint8 k61;
    uint8 k62;

    uint8 value6;

    ret = assign6(dest_array6,i6, j6, k6, l6, m6, n6, value, transient_array6, source_array6);
    require i6 < 5;
    require j6 < 5;
    require k6 < 5;
    require l6 < 5;
    require m6 < 5;
    require n6 < 5;
    require i61 < 5;
    require i61 != i6;
    require k61 < 5;
    require n61 < 5;
    require k62 < 5;
    require k62 != k6;
    require n62 < 5;
    require n62 != n6;

   
/**@title return array contains the content of the source array
* 
*/
   assert ret6 [i6][k6][n6] == value6;
   assert ret6 [i61][k61][n61] == dest_array6[i61][k61][n61];
   assert ret6 [i6][k62][n61] == transient_array6[j6][k6][n61];
   assert ret6 [i6][k6][n62] == source_array6[l6][m6][n62];
}


/// @title Assignment must change the data at specified index in dynamic destination array with value
rule assign7spec() {


    uint8[] dest_array7;
    uint8[] ret7;
    
    uint8 value7;
    uint8 i7;
    uint8 j7;
    
    ret7 = assign7(dest_array7, i7, value7);
     require i7 != j7;

/**@title return array contains the content of the source array
* 
*/
    assert ret7[i7] == value7;

/**@title return array contains the content of the destination array
* 
*/
    assert ret7[i7] == dest_array7[j7];
}

/// @title Assignment must change the data at specified index in destination 2D dynamic array with value
rule assign8spec() {


    uint8[] dest_array8;
    uint8[] ret8;
    
    uint8 value8;
    uint8 i8;
    uint8 j8;
    
    ret8 = assign8(dest_array, i8, value);
     require i8 != j8;

/**@title return array contains the content of the source array
* 
*/
    assert ret8[i8] == value8;

/**@title return array contains the content of the destination array
* 
*/
    assert ret8[i8] == dest_array8[j8];
}
