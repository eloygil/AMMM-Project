
# Python Instance Generator by Eloy Gil
# eloy.gil@est.fib.upc.edu
# MIRI - AMMM - FIB (UPC)

import sys, random, io
from time import gmtime, strftime


if __name__ == '__main__':
    try:
        nP = int(sys.argv[1])
    except:
        nP = 0

    random.seed(a=None)
    workTime = 720
    task = []
    task_window_min = []
    task_window_max = []
    dist = []
    filename = 'instance_' + str(nP) +'.dat'
    author = 'Eloy Gil Guerrero'
    email = 'eloy.gil@est.fib.upc.edu'
    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    if nP == 0:
        print 'ERROR: Invalid argument. (Aborting...)\n'
        print 'Usage: generator.py N\n'
        exit(0)
    else:
        print ('Creating instance with ', nP, 'points to visit, and a Starting/Ending one.')

    for i in range(0, nP):
        print i
        new_rand_val = str(random.getrandbits(100))[:2]
        # Task times generation
        if int(new_rand_val) > 50 or int(new_rand_val == 0):
            new_rand_val2 = new_rand_val[:2][1:]
            task.append(int(new_rand_val2) + 10)
        else:
            new_rand_val2 = new_rand_val[:2][1:]
            task.append(int(new_rand_val2))

        # Task window generation
        new_task_val = str(random.getrandbits(100))[:4][1:]
        while float(new_task_val) > workTime/2.7 or float(new_task_val) < workTime/11:
            new_task_val = str(random.getrandbits(100))[:2]
        task_range = int(new_rand_val[:2])
        while task_range < 40:
            task_range *= 1.21
        task_window_min.append(int(new_task_val))
        task_window_max.append(int(new_task_val) + int(task_range))

    # Distance matrix generation
    for x in range(0, nP+1):
        dist.append([])
        for y in range(0, nP+1):
            if x == y:
                dist[x].append(0)
            elif x > y:
                dist[x].append(dist[y][x])
            else:
                new_dist_val = str(random.getrandbits(100))[:4][1:]
                while float(new_dist_val) > workTime/6:
                    new_dist_val = str(random.getrandbits(100))[:4][1:]
                dist[x].append(int(new_dist_val))

    print "Generation completed."

    print "Results..."
    print "################################"
    print "Task: ", task
    print "Task start window:"
    print "Min: ", task_window_min
    print "Max: ", task_window_max
    print "Distance matrix:"
    print dist

    print "Exporting to file: ", filename
    with io.FileIO(filename, "w") as output:
        output.write('/*********************************************\n')
        output.write(' * OPL 12.6.0.0 Data\n')
        output.write(' * Author: ' + author + '\n')
        output.write(' * Email: ' + email + '\n')
        output.write(' * Creation Date: ' + date[8:10] + '/' + date[5:7] + '/' + date[:4] + ' at ' + date[11:] + '\n')
        output.write(' *********************************************/\n')
        output.write('\n')
        output.write('nP = ' + str(nP) + ';         // number of destination points \n')
        output.write('workTime = ' + str(workTime) + '; // maximum time to finish (12h in minutes) \n')
        output.write('\n')
        output.write('// time (minutes) spent in a task in each point \n')
        output.write('task = [ ')
        task_print = ''
        for i in range(0, len(task)):
            task_print += str(task[i]) + ' '
        task_print += '0 ];'
        output.write(task_print + '\n')
        output.write('\n')
        output.write('        	//  min   max\n')

        for i in range(0, len(task_window_min)):
            index = i + 1
            if i == 0:
                output.write('task_window = [[ ' + str(task_window_min[i]) + ' ' + str(task_window_max[i]) + ' ] // ' + str(index) + '\n')
            else:
                output.write('			   [ ' + str(task_window_min[i]) + ' ' + str(task_window_max[i]) + ' ] // ' + str(index) + '\n')
        output.write(']; \n')
        output.write('\n')
        output.write('	  //')
        for i in range(1, len(dist)):
            output.write('  ' + str(i))
        output.write('  S \n')
        for x in range(0, len(dist)):
            index = x + 1
            if index == nP + 1:
                index = 'S'
            if x == 0:
                output.write('dist = [[ ')
            else:
                output.write(' 	    [ ')
            for y in range(0, len(dist[x])):
                output.write(str(dist[x][y]) + ' ')
            output.write(' ] // ' + str(index) + '\n')
        output.write('];')

    print "Done."



