# Conversion Tool from verilog format to def format

## installation and usage:
 - clone the repo into the desired directory

 - inside the project directory: type in 

		python v2def [verilogfile] [leffile] [deffile]

 		(OR) ./v2def [verilogfile] [leffile] [deffile]

 - the program will internally use yosys library to generate a Gate Level Netlist and use it to parse the design logic.

## features:
you can add one of the following options:

 -a aspect_ratio

 -u core_utilization

 -s site_width

 -h row_height

 -mh horizontal_magin

 -mv vertical_magin

 -gnd layer,width

 -vdd layer,width

## Dependencies:
 - needs to have yosys library installed in device.

 - needs python 2.7 or similar version.

## Limitations:
 - doesnt support python 3 (you should receive an error message if you're not sure what version you are using).

 - the tool currently is considered to output a component-based format to be used incrementally afterwards in the design flow for placement
	and routing.

 - the tool reads both the technology file(lef) and design file(verilog) effeciently, but doesn't place the components on the die.

 - the special nets section also with the power rings included is not placed well. Only information about the metal layer and width is added  		in the design.

 - the tool assumes one top module per given verilog file; such top module becomes the design name in def.

 - the tool assumes that specialnets always include vdd and gnd.

## Example usage:
 - inside the project directory just type in:

 	./src/v2def tests/mux/mux4x1.v libs/osu035.lib libs/osu035.lef tests/mux/mux4x1.def -a 2 -gnd metal1,300 -vdd metal1,400

   1. this takes tests/mux/mux4x1.v libs/osu035.lib libs/osu035.lef as inputs. 
   
   2. this also specifies aspect ratio(width/height)=2; ground metal layer=metal1 with width=300; vdd metal layer=metal1 with width=400. 

   3. this should yield an output mux4x1.def file which you can see inside tests/mux.

## Passed Tests:
 - Tested on four designs mux4x1, uart, half_adder, and round_robin_arbiter (can be found in tests directoty).

 - The output def file was read correctly and verified using Glade IC Layout Tool.
 
 - The logs outputted from Glade with image of the Layout of each cell after importing its DEF file are both attached 
 	under each design's folder in tests directory.
	
 - The Glade library of all the 4 cells used in testing along with all cells extracted from osu035.lef file (can be seen in libs 	directory) is also attached insied tests directory.

