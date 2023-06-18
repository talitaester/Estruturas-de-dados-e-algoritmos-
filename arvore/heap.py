class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.past = None
    
    def showNode(self):
        return self.value
    
class Heap():
    def __init__(self):
        self.root = None

    