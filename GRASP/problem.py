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

    def load(self, path):
        self.nPoints = 0
        self.workTime = 0
        self.dist = []
        self.window = []
        self.task = []
        self.sourcePoint = self.nPoints
        self.bigM = self.workTime * 2
        file = open(path, "r")
        nPstr = "nP = "
        workTimeStr = "workTime = "
        taskStr = "task = ["
        taskWindowStr = "task_window = [["
        taskWindowLinesLeft = 0
        distStr = "dist = ["
        distLinesLeft = 0
        for line in file:
            if nPstr in line:
                # Gets the number of destination points (nP)
                self.nPoints = int(line.split(nPstr)[-1].split(";")[0])
                print "nP =", self.nPoints
            elif workTimeStr in line:
                # Gets the maximum workTime
                self.workTime = int(line.split(workTimeStr)[-1].split(";")[0])
                print "workTime =", self.workTime
            elif taskStr in line:
                # Get the task list
                tVal = line.split(taskStr)[-1].split(" ")
                for i in range(1,len(tVal)-1):
                    self.task.append(int(tVal[i]))
                print "task =", self.task
            elif taskWindowStr in line:
                # Gets the windows to perform tasks in each point, 1st line
                clean = line.split(taskWindowStr)[-1].split(']')[0].strip()
                self.window.append([int(clean.split(' ')[0]), int(clean.split(' ')[-1])])
                taskWindowLinesLeft = int(self.nPoints) - 1
            elif taskWindowLinesLeft > 0:
                # Gets the rest of lines for the window structure
                clean = line.split('[')[-1].split(']')[0].strip()
                self.window.append([int(clean.split(' ')[0]), int(clean.split(' ')[-1])])
                taskWindowLinesLeft -= 1
            elif distStr in line:
                # Gets the distance matrix, 1st line
                clean = line.split('[')[-1].split(']')[0].strip().split(" ")
                dist_file = []
                for v in clean:
                    if v != '':
                        dist_file.append(int(v))
                self.dist.append(dist_file)
                distLinesLeft = int(self.nPoints)
            elif distLinesLeft > 0:
                # Gets the rest of lines for the window structure
                clean = line.split('[')[-1].split(']')[0].strip().split(" ")
                dist_file = []
                for v in clean:
                    if v != '':
                        dist_file.append(int(v))
                self.dist.append(dist_file)
                distLinesLeft -= 1
        print "task_window =", self.window
        print "dist =", self.dist