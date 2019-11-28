# -*- coding: utf-8 -*- 

import copy  #deep copy를 위해 씀
import csv   #인쇄할 때 씀 

class block():

    waiting = []
    expanded = []
    idxInExpanded = -1

    def __init__(self, location):
        self.location = location
        self.row = location[0]
        self.col = location[1]
        self.heuristic = 10000000000000000

        block.waiting.append(self)
        self.myExpandedIdx = None
        self.prevIdx = 1000
        self.numChild = 0

    def calHeuristic(self, goal):
        return ((goal[0] - self.row)**2 + (goal[1] - self.col)**2 )**0.5

    def dfsExpand(self):
        global maze
        global mazeSize
        global time
        
        block.idxInExpanded += 1
        self.myExpandedIdx = block.idxInExpanded
        
        if(self.row-1 >= 1): 
            if maze[self.row-1][self.col] in ['2','4','6','5']:
                block([self.row-1,self.col])
                self.numChild += 1
                block.waiting[-1].prevIdx = self.myExpandedIdx
                if maze[self.row-1][self.col] != '4':
                    maze[self.row-1][self.col] = '7'
                time += 1   
        if(self.col-1 >= 0):
            if maze[self.row][self.col-1] in ['2','4','6','5']:
                block([self.row,self.col-1])
                self.numChild += 1
                block.waiting[-1].prevIdx = self.myExpandedIdx
                if maze[self.row][self.col-1] != '4':
                    maze[self.row][self.col-1] = '7'
                time += 1
        if self.row+1 <= mazeSize:
            if maze[self.row+1][self.col] in ['2','4','6','5']:
                block([self.row+1,self.col])
                self.numChild += 1
                block.waiting[-1].prevIdx = self.myExpandedIdx
                if maze[self.row+1][self.col] != '4':
                    maze[self.row+1][self.col] = '7'
                time += 1
        if self.col+1 <= mazeSize-1:
            if(maze[self.row][self.col+1] in ['2','4','6','5']):
                block([self.row,self.col+1])
                self.numChild += 1
                block.waiting[-1].prevIdx = self.myExpandedIdx
                if maze[self.row][self.col+1] != '4':
                    maze[self.row][self.col+1] = '7'
                time += 1
        
        block.expanded.append(block.waiting[-self.numChild-1])
        del block.waiting[-self.numChild-1]

    def greedyExpand(self, targetIdx, goal):
        global maze
        global mazeSize
        global time
        
        block.idxInExpanded += 1
        self.myExpandedIdx = block.idxInExpanded
        
        if(self.row-1 >= 1): 
            if maze[self.row-1][self.col] in ['2','4','6','5']:
                block([self.row-1,self.col])
                block.waiting[-1].prevIdx = self.myExpandedIdx
                block.waiting[-1].heuristic = block.waiting[-1].calHeuristic(goal)
                if maze[self.row-1][self.col] != '4':
                    maze[self.row-1][self.col] = '7'
                time += 1   
        if(self.col-1 >= 0):
            if maze[self.row][self.col-1] in ['2','4','6','5']:
                block([self.row,self.col-1])
                block.waiting[-1].prevIdx = self.myExpandedIdx
                block.waiting[-1].heuristic = block.waiting[-1].calHeuristic(goal)
                if maze[self.row][self.col-1] != '4':
                    maze[self.row][self.col-1] = '7'
                time += 1
        if self.row+1 <= mazeSize:
            if maze[self.row+1][self.col] in ['2','4','6','5']:
                block([self.row+1,self.col])
                block.waiting[-1].prevIdx = self.myExpandedIdx
                block.waiting[-1].heuristic = block.waiting[-1].calHeuristic(goal)
                if maze[self.row+1][self.col] != '4':
                    maze[self.row+1][self.col] = '7'
                time += 1
        if self.col+1 <= mazeSize-1:
            if(maze[self.row][self.col+1] in ['2','4','6','5']):
                block([self.row,self.col+1])
                block.waiting[-1].prevIdx = self.myExpandedIdx
                block.waiting[-1].heuristic = block.waiting[-1].calHeuristic(goal)
                if maze[self.row][self.col+1] != '4':
                    maze[self.row][self.col+1] = '7'
                time += 1
                
        block.expanded.append(block.waiting[targetIdx])
        del block.waiting[targetIdx]

def convert7to2():
    global maze
    for row in range(1,mazeSize):
        for col in range(0,mazeSize):
            if maze[row][col]=='7':
                maze[row][col]='2'

def readMaze(maze, filename):
    maze.clear()
    mazeFile = open(filename, "r")
    columns = mazeFile.readlines()
    for column in columns:
        column = column.split()
        row = [i for i in column]
        maze.append(row)

def writeMaze(finalMaze, filename):
    global length
    global time
    global mazeSize
    with open(filename, "w") as f:
        writer = csv.writer(f, delimiter=' ')

        writer.writerows(finalMaze)
        f.write("---\n")
        f.write("length = %d\n"%length)
        f.write("time = %d\n"%time)
        
def setKeyElement():
    global maze
    global mazeSize
    global length
    global time
    global start
    global key
    global goal
    
    start.clear()
    key.clear()
    goal.clear()
    length = 0
    time = 0
    mazeSize = int(maze[0][2])
    
    for row in range(1,mazeSize+1):
        for col in range(0,mazeSize):
            if maze[row][col]=='3':
                start.append(row)
                start.append(col)
            if maze[row][col]=='6':
                key.append(row)
                key.append(col)
            if maze[row][col]=='4':
                goal.append(row)
                goal.append(col)
                
def idxOfMinHeuristic():
    idxOfMin = 0
    for i in range(1,len(block.waiting)):
        if block.waiting[idxOfMin].heuristic >= block.waiting[i].heuristic:
            idxOfMin = i
    return idxOfMin 
    
def dfs(start, goal):
    block(start)
    while(len(block.waiting) != 0 and block.waiting[-1].location != goal):
        block.waiting[-1].dfsExpand()
    return -1

def greedy(start, goal):
    block(start)
    targetIdx = 0
    while(len(block.waiting) != 0 and block.waiting[targetIdx].location != goal):        
        block.waiting[targetIdx].greedyExpand(targetIdx, goal)
        targetIdx = idxOfMinHeuristic()
    return targetIdx

def findOptimalPath(start, targetIdx):
    global maze
    global length
    tempBlock = block.waiting[targetIdx]
    while(tempBlock.location != start):
        tempBlock = block.expanded[tempBlock.prevIdx]
        maze[tempBlock.row][tempBlock.col]='5'
        length += 1
    
def first_floor():
    global start, key, goal
    global maze, finalMaze 
    global mazeSize, length, time
       
    maze.clear()
    readMaze(maze, "first_floor.txt")
    setKeyElement()
    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1
       
    targetIdx = dfs(start, key)  
    findOptimalPath(start, targetIdx)
    convert7to2()
    finalMaze = copy.deepcopy(maze)
    
    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1

    targetIdx = dfs(key, goal)
    findOptimalPath(key, targetIdx)       
    
    for i in range(1,mazeSize):
        for j in range(0,mazeSize):
            if maze[i][j]=='5' or finalMaze[i][j]=='5':
                finalMaze[i][j]='5'
    finalMaze[start[0]][start[1]] = '3'

    finalMaze[start[0]][start[1]] = '3'
    del finalMaze[0]
    writeMaze(finalMaze, "first_floor_output.txt") 

def second_floor():
    global start, key, goal
    global maze, finalMaze 
    global mazeSize, length, time
     
    maze.clear()
    readMaze(maze, "second_floor.txt")
    setKeyElement()
    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1
        
    targetIdx = dfs(start, key)  
    findOptimalPath(start, targetIdx)

    convert7to2()
    finalMaze = copy.deepcopy(maze)
     
    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1

    targetIdx = dfs(key, goal)  
    findOptimalPath(key, targetIdx)     
    
    for i in range(1,mazeSize):
        for j in range(0,mazeSize):
            if maze[i][j]=='5' or finalMaze[i][j]=='5':
                finalMaze[i][j]='5'
    finalMaze[start[0]][start[1]] = '3'

    finalMaze[start[0]][start[1]] = '3'
    del finalMaze[0]
    writeMaze(finalMaze, "second_floor_output.txt") 
     
def third_floor():
    global start, key, goal
    global maze, finalMaze 
    global mazeSize, length, time

    maze.clear()
    readMaze(maze, "third_floor.txt")
    setKeyElement()
    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1
    
    targetIdx = greedy(start, key)  
    findOptimalPath(start, targetIdx)

    convert7to2()
    finalMaze = copy.deepcopy(maze)

    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1

    targetIdx = greedy(key, goal)
    findOptimalPath(key, targetIdx)    
   
    for i in range(1,mazeSize):
        for j in range(0,mazeSize):
            if maze[i][j]=='5' or finalMaze[i][j]=='5':
                finalMaze[i][j]='5'
    
    finalMaze[start[0]][start[1]] = '3'
    del finalMaze[0]
    writeMaze(finalMaze, "third_floor_output.txt")
 
def fourth_floor():
    global start, key, goal
    global maze, finalMaze 
    global mazeSize, length, time

    maze.clear()
    readMaze(maze, "fourth_floor.txt")
    setKeyElement()
    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1
       
    targetIdx = greedy(start, key)  
    findOptimalPath(start, targetIdx)
      
    convert7to2()
    finalMaze = copy.deepcopy(maze)

    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1

    targetIdx = greedy(key, goal)
    findOptimalPath(key, targetIdx)       
   
    for i in range(1,mazeSize):
        for j in range(0,mazeSize):
            if maze[i][j]=='5' or finalMaze[i][j]=='5':
                finalMaze[i][j]='5'

    finalMaze[start[0]][start[1]] = '3'
    del finalMaze[0]
    writeMaze(finalMaze, "fourth_floor_output.txt")  

def fifth_floor():
    global start, key, goal
    global maze, finalMaze 
    global mazeSize, length, time

    maze.clear()
    readMaze(maze, "fifth_floor.txt")
    setKeyElement()
    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1
       
    targetIdx = greedy(start, key)  
    findOptimalPath(start, targetIdx)
      
    convert7to2()
    finalMaze = copy.deepcopy(maze)

    block.waiting.clear() 
    block.expanded.clear()
    block.idxInExpanded = -1

    targetIdx = greedy(key, goal)
    findOptimalPath(key, targetIdx)       
   
    for i in range(1,mazeSize):
        for j in range(0,mazeSize):
            if maze[i][j]=='5' or finalMaze[i][j]=='5':
                finalMaze[i][j]='5'

    finalMaze[start[0]][start[1]] = '3'
    del finalMaze[0]
    writeMaze(finalMaze, "fifth_floor_output.txt") 
 
###########################################

maze = []
finalMaze = []
mazeSize = 0
start = []
key = []
goal = []
time = 0
length = 0

first_floor()
second_floor()
third_floor()
fourth_floor()
fifth_floor()
