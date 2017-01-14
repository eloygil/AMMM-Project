'''
Python Instance Generator by Eloy Gil
eloy.gil@est.fib.upc.edu
MIRI - AMMM - FIB (UPC)
'''

import sys
try:
    nP = sys.argv[1]
except:
    nP = 0
if nP == 0:
    print 'ERROR: Invalid parameter.\n'
    print 'Usage: generator.py N\n'
else:
    print args.accumulate(args.integers)