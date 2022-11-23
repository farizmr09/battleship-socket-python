import random

class Game:
    def __init__(self):
        self.board = [ [0]*8 for i in range(8)]
        self.oppBoard = [ ['x']*8 for i in range(8)]

    def shipRandom(self):
        self.shipLenghts = [5, 4, 3, 2, 2]
        for ship in self.shipLenghts:    
            ori = random.randint(0, 1) # 0 == horizontal && 1 == vertical
            coord = [random.randint(0, 7), random.randint(0, 7)]
            valid = self.checkValid(ori, coord, ship)
            while valid != True:
                ori = random.randint(0, 1) # 0 == horizontal && 1 == vertical
                coord = [random.randint(0, 7), random.randint(0, 7)]
                valid = self.checkValid(ori, coord, ship)
            self.setShip(ori, coord, ship)
    
    def setShip(self, ori, coord, ship):
        for i in range(ship):
            if ori == 0:
                self.board[coord[0] + i][coord[1]] = 1
            else:
                self.board[coord[0]][coord[1] + i] = 1

    def checkValid(self, ori, coord, ship):
        if(ori == 0): #horizontal
            if(coord[0] + ship > 8):
                return False
            for i in range(coord[0], coord[0] + ship):
                if self.board[i][coord[1]] == 1:
                    return False
        if(ori == 1): #vertical
            if(coord[1] + ship > 8):
                return False
            for i in range(coord[1], coord[1] + ship):
                if self.board[coord[0]][i] == 1:
                    return False
        return True

    def printBoard(self):
        print("   Your board            Opp's board")
        for i in range(8):
            for j in range(2):
                for k in range(8):
                    if k == 0:
                            print(f"{7-i}  ", end="")
                    if j == 0:
                        print(f"{self.board[i][k]} ", end="")
                        if k == 7:
                            print("   ", end="")
                    else:
                        print(f"{self.oppBoard[i][k]} ", end="")
                        if k == 7:
                            print()
        print()
        print("   0 1 2 3 4 5 6 7       0 1 2 3 4 5 6 7")
        print()






