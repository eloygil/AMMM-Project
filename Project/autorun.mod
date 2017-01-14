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
	cplex.epgap=0.01;

	for (var i = 5; i <= 5; i += 1) {
		for (var j = 1; i <= 2; i += 1) {
			var filename = "./../InstanceGen/instance_" + i + ".dat";
			var model = new IloOplModel(def, cplex);
			var data = new IloOplDataSource(filename);
			model.addDataSource(data);
			model.generate();
			if (cplex.solve()) {
				writeln("Found solution for "+ filename +" execution number "+j);
				writeln("Objective function value: " + cplex.getObjValue());
				writeln("Execution time " + cplex.getSolvedTime());
			}
			else writeln("No solution for "+filename+" execution number "+j);
		}
	}
}