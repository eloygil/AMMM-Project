/*********************************************
 * OPL 12.6.0.0 Model
 * Author: Eloy
 * Creation Date: 26/10/2016 at 18:00:39
 *********************************************/
int nP = ...;
int S = nP+1;
int nT = ...;
int workTime = ...;

range T = 1..nT;
range P_s = 1..nP;
range P = 1..S; 

float dist[p in P][q in P] = ...;
float task[p in P] = ...;
 
dvar float+ arrive_pt[p in P_s][t in T];
dvar float+ end_time[t in T];
dvar boolean pt[p in P][t in T];
dvar boolean from_p_to_q[t in T][p in P][q in P];

minimize max(t in T) end_time[t];

subject to {
	
	// Constraint 1 (no time travelling allowed between two points)
	// Aqui esta el problema si lo pones no funsiona 
	forall (p in P_s, q in P_s)
		forall (t in T)
			arrive_pt[q][t] - arrive_pt[p][t] >= (from_p_to_q[t][p][q] * (dist[p][q] + task[p])) - (9999999 * (1-from_p_to_q[t][p][q]));
	
	forall (p in P_s, t in T) {
		arrive_pt[p][t] >= from_p_to_q[t,S,p] * dist[S][p];
		end_time[t] >= arrive_pt[p][t] + (from_p_to_q[t][p][S] * (dist[p][S] + task[p]));
    }	  
    
	// Constraint 4 (worktime behind maximum)
	forall (t in T)
	  	end_time[t] <= workTime;	
		
	// Constaint 6 and 7 (se visitan todos los puntos (excepto el origen) una sola vez y define el orden)
	forall (p in P_s)
		sum(t in T) pt[p,t] == 1;
		
	forall (t in T, p in P) {
		pt[S][t] >= pt[p][t];	
		from_p_to_q[t,p,p] == 0;
		sum(q in P) from_p_to_q[t,p,q] == pt[p][t];
		sum(q in P) from_p_to_q[t,q,p] == pt[p][t];		
	}		
}
