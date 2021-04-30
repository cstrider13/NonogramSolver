class NonoLine:
    def __init__(self, size, SideOrTop, data):
        self.size = size
        self.SideOrTop = SideOrTop
        self.data = data

class Nonogram:
    def __init__(self, height, width, SideLines, TopLines):
        self.height = height
        self.width = width
        self.SideLines = SideLines
        self.TopLines = TopLines
        self.filled = [[u"\u25A1"] * width for i in range(height)]
        #if we know square is supposed to be empty, make it -1
        
    def solve(self):
        self.firstSolve()#check this first
        print("Filled after first solve")
        for i in range(len(self.filled)):
            print(self.filled[i])
        self.edgeSolve()
        print("Filled after edge solve")
        for i in range(len(self.filled)):
            print(self.filled[i])
        #TODO: fill in Xs if a row if done
        self.XSolve()
        print("Filled after X solve")
        for i in range(len(self.filled)):
            print(self.filled[i])
        
    def XEdgeSolve():#solve when you are bordered by an X
        
        
    def XSolve(self):
        for i in range(self.height):#Rows
            rowSum = 0
            rowSumNeed = 0
            for j in range(self.width):
                if self.filled[i][j] == u"\u25A0":
                    rowSum += 1
            for j in range(len(self.SideLines[i])):
                rowSumNeed += self.SideLines[i][j]
            if rowSumNeed == rowSum:
                #X out rest
                for j in range(self.width):
                    if self.filled[i][j] != u"\u25A0":
                        self.filled[i][j] = 'X'
            
    def edgeSolve(self): #fill edges
        #first, check left edge
        for i in range(self.height):
            if self.filled[i][0] == u"\u25A0":
                end = 0
                for j in range(self.SideLines[i][0]):
                    self.filled[i][j] = u"\u25A0"
                    end = j
                if (end+1) <= (self.width - 1):#if it isn't the end, put X
                    self.filled[i][end+1] = 'X'#-1
        #Next, check the top
        for i in range(self.width):
            if self.filled[0][i] == u"\u25A0":
                end = 0
                for j in range(self.TopLines[i][0]):
                    self.filled[j][i] = u"\u25A0"
                    end = j
                if (end+1) <= (self.height - 1):#if it isn't the end, put X
                    self.filled[end+1][i] = 'X'
        #Next, check the right
        right = self.width-1
        for i in range(self.height):
            if self.filled[i][right] == u"\u25A0":
                end = 0
                for j in range(self.SideLines[i][len(self.SideLines[i])-1]):
                    self.filled[i][right-j] = u"\u25A0"
                    end = j
                if (right-(end+1)) >= (0):#if it isn't the end, put X
                    self.filled[i][right-(end+1)] = 'X'
            #print("Right filled")
            #for x in range(len(self.filled)):
            #    print(self.filled[x])
        #Finally, check the bottom
        bot = self.height - 1
        for i in range(self.width):#len(self.SideLines[bot])):
            if self.filled[bot][i] == u"\u25A0":
                end = 0
                for j in range(self.TopLines[i][len(self.TopLines[i])-1]):
                    self.filled[bot-j][i] = u"\u25A0"
                    end = j
                if (bot-(end+1)) >= (0):#if it isn't the end, put X
                    self.filled[bot-(end+1)][i] = 'X'
        
    def firstSolve(self):#first check for solving
        #check side
        for i in range(len(self.SideLines)):
            #These checks are for if the input is 1 long
            if len(self.SideLines[i]) == 1:
                #Check if input is same as size
                if self.SideLines[i] == self.width:
                    for j in range(self.width):
                        self.filled[i][j] = u"\u25A0"
                #Check if row is empty
                if self.SideLines[i] == 0:
                    for j in range(self.width):
                        self.filled[i][j] = 'X'#these are known to be Xs
            else:
                #These check are for if the input is > 1 long
                #Check if the inputs add up to the row
                rowSum = 0
                for j in range(len(self.SideLines[i])):
                    rowSum += self.SideLines[i][j]
                if (rowSum + (len(self.SideLines[i]) - 1)) == self.width:
                    idx = 0
                    for j in self.SideLines[i]:
                        for x in range(j):
                            self.filled[i][idx] = u"\u25A0"
                            idx += 1
                        #if it's not the end, put an X
                        if idx <= (self.width - 1):
                            self.filled[i][idx] = 'X'
                            idx += 1

        #Check top
        for i in range(len(self.TopLines)):
            #These checks are for if the input is 1 long
            if len(self.TopLines[i]) == 1:
                #Check if input is same as size
                if self.TopLines[i] == self.height:
                    for j in range(self.height):
                        self.filled[j][i] = u"\u25A0"
                #Check if row is empty
                if self.TopLines[i] == 0:
                    for j in range(self.height):
                        self.filled[j][i] = 'X'#these are known to be Xs
            else:
                #These check are for if the input is > 1 long
                #Check if the inputs add up to the row
                colSum = 0
                for j in range(len(self.TopLines[i])):
                    colSum += self.TopLines[i][j]
                if (colSum + (len(self.TopLines[i]) - 1)) == self.height:
                    idx = 0
                    for j in self.TopLines[i]:
                        for x in range(j):
                            self.filled[idx][i] = u"\u25A0"
                            idx += 1
                        #if it's not the end, put an X
                        if idx <= (self.height - 1):
                            self.filled[idx][i] = 'X'
                            idx += 1

        
#Set up a line
#10 x 10
sideData = [[1,1,6], [1,7], [4,3], [2,1], [1,2], [1,1,1], [4,2], [3], [3,3], [2,1]]
topData = [[2], [1], [1,1,1,1], [8], [4,3], [3,1,1], [2,1], [3,2], [3,1,1,1], [7,2]]
#(self, height, width, SideLines, TopLines
testGram = Nonogram(10, 10, sideData, topData)
testGram.solve()
