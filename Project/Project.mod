/*********************************************
 * OPL 12.6.0.0 Model
 * Author: Eloy Gil Guerrero
 * Email: eloy.gil@est.fib.upc.edu
 * Creation Date: 26/10/2016 at 18:00:39
 *********************************************/
int nP = ...;
int S = nP+1;
int nT = nP;
int workTime = ...;
int bigM = workTime * 2;

range T = 1..nT;
range P_s = 1..nP;
range P = 1..S;
range window = 1..2;

float dist[p in P][q in P] = ...;
float task[p in P] = ...;
float task_window[p in P_s][w in window] = ...;
 
dvar float+ arrive_pt[p in P_s][t in T];
dvar float+ end_time[t in T];
dvar boolean pt[p in P][t in T];
dvar boolean from_p_to_q[t in T][p in P][q in P];

// La fila S de pt te dice los camiones que salen y los que no, lo multiplicamos por bigM para darle mas importancia,
// si dos soluciones empatan ("sum(t in T) pt[S][t] * bigM" tiene el mismo valor en ambas) se desempata sumándole 
// el tiempo maximo de llegada
minimize (sum(t in T) pt[S][t] * bigM) + (max(t in T) end_time[t]);

subject to {
	
	// Constraint 1 (no time travelling allowed between two points)
	// The time difference between the arriving time at the 2nd point and the arriving time at the 1st is bigger than the distance 
	// between the 1st and the 2nd point plus the time spent in the task, if such a track actually exists. Otherwise this comparison is
	// avoided using the bigM value that is a way bigger negative value.
	forall (p in P_s, q in P_s)
		forall (t in T)
			arrive_pt[q][t] - arrive_pt[p][t] >= (from_p_to_q[t][p][q] * (dist[p][q] + task[p])) - (bigM * (1-from_p_to_q[t][p][q]));
			
	// Constraint 2 (same as Constraint 1 but for the special cases of Source/Destination point)
	forall (p in P_s, t in T) {
		// Departure
		arrive_pt[p][t] >= from_p_to_q[t,S,p] * dist[S][p];
		// Arrival
		end_time[t] >= arrive_pt[p][t] + (from_p_to_q[t][p][S] * (dist[p][S] + task[p]));
	}
	
	// Constaint 3 (task started during the specified time window)
	forall (p in P_s, t in T) {		
		arrive_pt[p][t] >= task_window[p][1] * pt[p][t];
		arrive_pt[p][t] <= task_window[p][2] * pt[p][t];	
    }	  
    
	// Constraint 4 (worktime behind maximum)
	forall (t in T)
	  	end_time[t] <= workTime;	
		
	// Constaint 5 (each point is visited exactly once, except the Source/Destination point) 
	forall (p in P_s)
		sum(t in T) pt[p,t] == 1;
		
	// Constraint 6 (defines the order of the visits)
	forall (t in T, p in P) {
		// If truck t visits any point it also visits the Source/Destination point
		pt[S][t] >= pt[p][t];
		// Avoids to travel from a point to itself.	
		from_p_to_q[t,p,p] == 0;
		// If truck t visits a point p it must have a previous and next point
		sum(q in P) from_p_to_q[t,p,q] == pt[p][t];
		sum(q in P) from_p_to_q[t,q,p] == pt[p][t];		
	}
}
execute {
   // Postprocessing
	printing = 1;
	if (printing == 1) {
		var t_used = 0;
	  	for (var t in T) {  	
	  	  	if (pt[S][t] == 1) {
	  	  	  	t_used += 1;
		  		write("Route for truck " + t + ": [ S ");
		  		var destination = 0;  		
		  		for (var p in P_s) {
		  			if (from_p_to_q[t][S][p] == 1) {
		  				write(p + " ");		
		  				destination = p;		
		  			}
		  		}
				while (destination != S) {
	  				for (var p in P) {
		  				if (from_p_to_q[t][destination][p] == 1) {
		  					if (p == S) write("S ");		  					
		  					else write(p + " ");	  							
		  					destination = p;		
		  				}
	    			}  				
	  			}
	  		writeln("]");
	  		}
		}
		var last_time = 0;
		for (var t in T) {
			if (end_time[t] > last_time) last_time = end_time[t];
		}	
		writeln("Total trucks used: " + t_used);
		writeln("Last truck arrives at: " + last_time);
	}		
}