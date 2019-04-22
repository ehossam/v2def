/*******************************************************************
*
* Module: HA.v
* Project: Half_Adder
* Author: Hossam Elsamanoudy (samanoudy@aucegypt.edu)
* Description: Half_Adder_Implementation
*
* Change history: 02/20/19 – Implementation of the module 		  
*
**********************************************************************/
`timescale 1ns/1ns
/* just a simple half adder implementation */

module HA(input a, 
          input b,
          output s,
          output co);
 
     xor xor1 (s,a,b);
     and and1 (co,a,b);
                 
endmodule

