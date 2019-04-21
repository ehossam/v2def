# Conversion Tool from verilog format to def format

## installation and usage:
 -clone the repo into the desired directory
 -inside src directory: type in 
	python v2def [verilogfilename] [leffile] [deffile]
 	(OR) ./v2def [verilogfilename] [leffile] [deffile]

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
 -needs to have yosys library installed in device
 -needs python 2.7 or similar version

## Limitations:
 -doesnt support python 3 (you should receive an error message if you're not sure what version you are using)
 -the tool reads both the technology file(lef) and design file(verilog) effeciently, but doesn't place the components on the die 	very well; just initial estimation is being outputted here
 -the special nets section also with the power rings included is not placed well. Just initial estimation.
