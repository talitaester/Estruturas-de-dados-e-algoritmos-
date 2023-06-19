class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
 
    
    def showNode(self):
        return self.value
class listES:
    def __init__(self, max):
        self.head = None
        self.size = 0
        self.max = max
        self.objList = [None] * max


    def insertES(self, no):
        if self.size == 0:
           self.objList[0] = no
           self.head = no
           self.size += 1
        elif self.size < self.max:
           self.objList[self.size] = no
           self.size += 1
    
    def showList(self):
      for i in self.objList:
        print(i)
class Tree:
    def __init__(self):
        self.root = None
        self.height = 0


    def insert(self, node)