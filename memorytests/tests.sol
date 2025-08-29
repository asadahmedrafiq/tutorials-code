// SPDX-License-Identifier: MIT
// Memory test for assignment behavior (/certora/tutorials-code/memorytests/tests.sol)

pragma solidity ^0.8.0;


/**
 * @dev Implementation of assignment behavior of memroty variables in Solidity
 */
contract tests {
   
    constructor() {
    }
//[[[0,0],[1,1]],[[2,2],[3,3]]]
//[[[4,4],[5,5]],[[6,6],[7,7]]]
//[[[8,8],[9,9]],[[10,10],[11,11]]]
//i=0
//j=0
//l=0
//l=0
//"uint8[2][2][2]: 100,4,5,5,2,2,3,3"
 function t06(uint8[2][2][2] memory x4, uint8 i4, uint8 j4, uint8 k4, uint8 l4, uint8 value4, uint8[2][2][2] memory y4) 
    pure
    public 
    returns (uint8[2][2][2] memory)  
    {
      x4[i4] = y4[j4];
      y4[j4][k4][l4] = value4;
      return x4;
    }

/*
 [   
          [
              [ [1, 2], [3, 4] ],     
              [ [5, 6], [7, 8] ]      
        ],
        [   
            [ [9, 10], [11, 12] ],  
            [ [13, 14], [15, 16] ]  
        ]
    ]
*/
/*
[   
         [
             [ [6, 6], [7, 7] ],     
            [ [4, 4], [5, 5] ]      
        ],
        [   
            [ [0, 0], [1, 1] ],  
            [ [2, 2], [3, 3] ]  
        ]
    ]
*/
//i=0
//j=0
//l=0
//l=0
    
function t07(uint8[2][2][2][2] memory x5, uint8 i5, uint8 j5, uint8 k5, uint8 l5, uint8 value5) 
    pure 
    public 
    returns (uint8[2][2][2][2] memory)  
    {
      x5[i5][j5][k5][l5] = value5;
      return x5;
    }

/*
[
  [0,0], 
  [1,1]
]
*/
/*
[
  [2,2], 
  [3,3]
]
*/
//1=0,j=0,k=0, value = 100
//"uint8[2][2]: 100,2,1,1"
  function t09(uint8[2][2] memory x6, uint8 i6, uint8 j6, uint8 k6, uint8 value6, uint8[2][2] memory y6) 
    pure 
    public 
    returns (uint8[2][2] memory)  
    {
      x6[i6] = y6[j6];
      y6[j6][k6] = value6;
      return x6;
    }


function t08(uint8[2][2][2][2] memory x51, uint8 i51, uint8 j51, uint8 k51, uint8 l51, uint8 m51, uint8 value51, uint8[2][2][2][2] memory y51) 
    pure 
    public 
    returns (uint8[2][2][2][2] memory)  
    {
      x51[i51] = y51[j51];
      y51[j51][k51][l51][m51] = value51;
      return x51;
    }

 function t14(uint8[][] memory x8, uint8 i8, uint8 j8, uint8 k8, uint8 value8, uint8[][] memory y8) 
    pure 
    public 
    returns (uint8[][] memory)  
    {
     x8[i8] = y8[j8];
      y8[j8][k8] = value8;
      return x8;
    }

    
 function t11(uint8[2][2][2] memory x8, uint8 i8, uint8 j8, uint8 k8, uint8 l8, uint8 m8, uint8 n8, uint8 value8, uint8[2][2][2] memory y8, uint8[2][2][2] memory z8) 
    pure
    public 
    returns (uint8[2][2][2] memory)  
    {
      x8[i8] = y8[j8];
      y8[j8][k8] = z8[l8][m8];
      z8[l8][m8][n8]= value8;
      return x8;
    }
   }
