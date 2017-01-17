# -*- coding: utf-8 -*-
'''
GRASP Solver by Eloy Gil
eloy.gil@est.fib.upc.edu
'''

class Problem(object):
    def __init__(self):
        self.workTime = 720
        self.nPoints = 6
        self.dist = [[    0,    82,   103,    17,   110,    26,    23  ], # 0
                    [    82,     0,     3,    46,    52,     1,     2  ], # 1
                    [   103,     3,     0,   120,    74,    41,   111  ], # 2
                    [    17,    46,   120,     0,     2,    31,    99  ], # 3
                    [   110,    52,    74,     2,     0,    27,    61  ], # 4
                    [    26,     1,    41,    31,    27,     0,    85  ], # 5
                    [    23,     2,   111,    99,    61,    85,     0  ]] # S
        self.window =  [[  124,  181 ], # 0
                        [   90,  169 ], # 1
                        [   79,  156 ], # 2
                        [   77,  165 ], # 3
                        [   83,  128 ], # 4
                        [   86,  183 ]] # 5
        self.task = [ 17, 19, 17, 18, 2, 17, 0 ]
        self.sourcePoint = self.nPoints
        self.bigM = self.workTime * 2


