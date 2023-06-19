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


    def insert(self, node, pos):

        if self.root is None:
            self.root = node
        else:

            if pos.left is None:
                pos.left = node
            elif pos.right is None:
                pos.right = node
            else:
                self.insert(node, pos.left)



    
    def inOrder(self, no):
        if no is not None:
            self.inOrder(no.left)
            print(no.value)
            self.inOrder(no.right)
        

def main():
    tree =  Tree()
    valores = input().split()
    [int(x) for x in valores]
    for i in valores:
        tree.insert(Node(i), tree.root)

    tree.inOrder(tree.root)


if __name__ == '__main__':
    main()
