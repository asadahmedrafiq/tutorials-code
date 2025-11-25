/**
 *This is specification file for initializationd1n1.sol (initializationd1n1spec.spec).
 * Run using:
 *
 * certoraRun /home/asad/certora/tutorials-code/memorytests/initializationd1n1.sol --verify initializationd1n1:/home/asad/certora/tutorials-code/memorytests/initializationd1n1spec.spec
 *
 * There should be no errors.
 */
   /**Test results: 
 *          Result: pass
 */
methods
{
    // Declare function for a method
    function initializationd1n1f (bool[1]) external returns (bool[1] memory) envfree;
}


rule initializationd1n1rule() {


    bool[1] dummy_array;
    bool[1] ret;
    
   
    require dummy_array [0] == false ;
   
    
   ret = initializationd1n1f (dummy_array);
  
   assert ret[0] == false;
}