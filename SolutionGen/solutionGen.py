'''
Python Solver Solution Generator v1.0
Copyright 2016 Eloy Gil.
'''

import sys, os

if __name__ == '__main__':
    for line in open(sys.argv[1],'r').readlines():
        c_line = line.replace("\n", "")
        print 'Executing: ' + line
        os.system('python ../GRASP/main.py ' + c_line)
        print 'Finished. \n'
    sys.exit()