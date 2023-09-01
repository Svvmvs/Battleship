import logging

logging.basicConfig(filename="logging_spot1.txt", filemode='w', datefmt='%H:%M:%S', level=logging.DEBUG)

#I suppse the board will need a name?
#I am using -100 and -110 as nulls here, because I didn't want to make actual nulls.
    #having nulls lets us do A5 rather than Ax+1 or something like that.
    #so it'd be board.A[5] or board.tile[LtoI('A')][5] or something like that, assuming we have a LtoI that changes A to 1
    #  I like the first better.

class board1(object):
    def __init__(self, name):
        self.name = name
        self.A = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.B = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.C = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.D = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.E = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.F = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.G = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.H = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.I = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.J = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class board2(object):
    def __init__(self, name):
        self.name = name
        self.tile = [-110, 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [-100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]