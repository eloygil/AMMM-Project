/*********************************************
 * OPL 12.6.0.0 Automated Execution Script
 * Author: Eloy Gil Guerrero
 * Email: eloy.gil@est.fib.upc.edu
 * Creation Date: 13/01/2017 at 12:31:22
 *********************************************/
 
main {
	var src = new IloOplModelSource("Project.mod");
	var def = new IloOplModelDefinition(src);
	var cplex = new IloCplex();
	cplex.epgap = 0.01;
	writeln("Starting...")

	for (var i = 5; i <= 18; i += 1) {
		for (var j = 1; j <= 3; j += 1) {
			var filename = "../InstanceGen/instance_"+i+".dat";
			var opl = new IloOplModel(def, cplex);
			var data = new IloOplDataSource(filename);
			opl.addDataSource(data);
			opl.generate();
			if (cplex.solve()) {			
				writeln("Found solution for instance_" +i+".dat #"+j);
				writeln("Objective function value: "+cplex.getObjValue());
				writeln("Execution time: "+cplex.getSolvedTime());
			}
			else writeln("No solution for "+filename + " execution number "+j);
		}
	}
}