# MIRI-AMMM Course Project by Eloy Gil - Q1 2016-17 FIB (UPC)
# Contact: eloy.gil@est.fib.upc.edu

1. Instance generation: There is a Python generator in InstanceGen/generator.py, 
it creates instances that are compatible with CPLEX and GRASP/BRKGA solvers. 
Script usage: generator.py N N: Positive integer, represents the number of 
destination points to create Output: instance_N.dat file in the same directory. 
 
2. OPL model execution: The model is located at Project/Project.mod, it can be 
manually executed in CPLEX adding any of the instances previously generated or 
new ones. Also, there is a script in Project/autorun.mod that can be used to 
execute different instances many times to extract an average. 
 
3. GRASP/BRKGA execution: The manual way consists in executing GRASP/main.py 
with the following arguments: 
	1st: Path to instance (ex. '../InstanceGen/instance_6.dat') 
	2nd: Solver selected ( GRASP-BI | GRASP-FI | BRKGA ) 
	3rd: Target execution time (in seconds) 
Example: main.py ../InstanceGen/instance_6.dat BRKGA 30 
 
4. Batch execution script: Alternative to manual execution for GRASP and BRKGA.  
It is in: SolutionGen/solutionGen.py 
Script usage: solutionGen.py batchinputfile > outputfile 
The input files must be the relative path to the main.py script and its 
arguments. Check SolutionGen/input/*.txt files to see some examples of the 
expected content of the input files for this script.  
 
5. Result extraction script: Makes easier to copy & paste results to the Excel 
spreadsheet. It is in: SolutionGen/solutionExt.py 
Script usage: solutionExt.py outputfile It shows the number of vehicles (NT) 
needed in every solution and also the objective function value (Q). 
 
6. Graph generation: The Excel file Project/graph.xlsx is a spreadsheet used to 
generate the different figures and also store and compare the results obtained.  