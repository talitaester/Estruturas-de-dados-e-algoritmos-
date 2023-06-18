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

    def clearTree():
        self.root = None

    def insert(self, no, pos):
        if self.root is None:
            self.root = no
        else:
            if pos.right is None:
                pos.right = no
            elif pos.left is None:
                pos.left = no
            else:
                if (pos.right.right is None) or (pos.right.left is None):
                    self.insert(no, pos.right)
                elif (pos.left.right is None) or (pos.left.left is None):
                    self.insert(no, pos.left)
                else:
                    self.insert(no, pos.right)
    

    def nodeDepth(self, value):
        if self.root is None:
            return 0
        return self._nodeDepth(self.root, value)
    

    def _nodeDepth(self, value):
        if self.root is None:
            return -1  # Valor de altura inválido para indicar que o nó não foi encontrado
        
        node, found = self.preOrder(self.root, value)
        if found:
            return self.treeHeight(node) 

        return 0 

        

    def callTreeHeight(self):
        if self.root is None:
            return 0
        else:
            height =  self.treeHeight(self.root)
            return height
        
    def max2(self, value1, value2):
        if value1 >= value2:
            return value1
        else:
            return value2

    def treeHeight(self, pos):
        if pos is None or (pos.right is None and pos.left is None):
            return 0
        else:
            leftHeight = 1 + self.treeHeight(pos.left)
            rightHeight = 1 +  self.treeHeight(pos.right)

            return self.max2(leftHeight, rightHeight)




    def preOrder(self, no, key):
        if (int(no.value) == key):
            return no, True
    
        if no is not None:
            if no.right is not None:
                no1, found = self.preOrder(no.right, key) 
                if found is True:
                    return no1, True
            if no.left is not None:
                no2, found = self.preOrder(no.left, key)  
                if found is True:
                    return no2, True
                
        return no, False
    

    def findTwoValues(self, no1, no2, tree_height):  
        
        node1, found1 = self.preOrder(self.root, no1)
        node2, found2 = self.preOrder(self.root, no2)
        if found1:
            print('FOUND IT 1')
        if found2:
            print('FOUND IT 2')    
        height1 = self.treeHeight(node1)
        height2 = self.treeHeight(node2)
        print(height1, height2)
        if (found1 is True) and (found2 is True):
            gap = height1 - height2
            if gap < 0:
                gap = -gap
            return gap
        elif found1 is True:

            return height1 
        elif found2 is True:
            return height2
        else:
            return tree_height
        
            


def main():
    arvore = Tree()
    lines = int(input())
    elementos = input().split()
    for i in elementos:
        no = Node(i)
        arvore.insert(no, arvore.root)
    altura = arvore.callTreeHeight()
    print('altura', altura)

    result_list = listES(lines-1)

    for i in range(lines-1):
        value1, value2 =  input().split()
        value1= int(value1)
        value2= int(value2)
        res = arvore.findTwoValues(value1, value2, altura)
        result_list.insertES(res)
        
    result_list.showList()

if __name__ == '__main__':
    main()

    