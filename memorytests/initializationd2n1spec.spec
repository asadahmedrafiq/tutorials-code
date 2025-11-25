/**
 * This is specification file for initializationd2n1.sol (initializationd2n1spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/initializationd2n1.sol --verify initializationd2n1:/home/asad/certora/tutorials-code/memorytests/initializationd2n1spec.spec
 *
 * There should be no errors.
 */
  */
   /**Test results: 
 *          Result: pass
 */
methods
{
    // Declare function for a method
    function initializationd2n1f(bool[1][1]) external returns (bool[1][1] memory) envfree;
}


rule initializationd2n1rule() {


    bool[1][1] dummy_array;
    bool[1][1] ret;
    
   
    require dummy_array [0][0] == false ;
   
    
   ret = initializationd2n1f(dummy_array);
  
   assert ret[0][0] == false;
}