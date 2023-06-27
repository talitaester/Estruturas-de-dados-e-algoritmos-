class listES:
    def __init__(self, max):
        self.head = None
        self.size = 0
        self.max = max
        self.objList = [None] * max

    def insert(self, no):
        if self.size == 0:
           self.objList[0] = no
           self.head = no
           self.size += 1
        elif self.size < self.max:
           self.objList[self.size] = no
           self.size += 1

    def showList(self):
      for i in self.objList:
        if i is not None:
            print(i)

class treeNode:
    def __init__(self, maxKeys):
        self.maxKeys = maxKeys
        self.values = listES(maxKeys)
        self.keysAmount = self.values.size
        self.left = None
        self.right = None
        self.parent = None



class bTree:
    def __init__(self) -> None:
        self.root = None

    def inser(self, value):
        if self.root is None:
            self.root = treeNode(self.maxKeys)
            self.root.insert(value)
        else:
            
            

           
       
