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


    def insert(self, no):
        if self.size == 0:
           self.objList[0] = no
           self.head = no
           self.size += 1
        elif self.size < self.max:
           self.objList[self.size] = no
           self.size += 1
                 
    def showList(self, stop):
      for i in self.objList:
            print(i, end=' ')
            if i == stop:
                break

    def delList(self):
       i = 0
       while i < self.size:
          self.objList[i] = None
          i += 1
          self.size -= 1

class Tree:
    def __init__(self, size):
        self.root = None
        self.size =  size
        #essa é uma lista estática que serve apenas para auxiliar no print dos valores.
        self.elements = listES(size)

    def refresh(self):
        self.elements = listES(self.size)

    def insert(self, no, pos):
        if self.root is None:
            self.root = no
        else:
            if no.value >= pos.value:
                if pos.right is None:
                    pos.right =  no
                else:
                    self.insert(no, pos.right)
            else:
                if pos.left is None:
                    pos.left =  no
                else:
                    self.insert(no, pos.left)

    def inOrder(self, no, value):
        if no is not None:
            self.inOrder(no.left, value)
            self.elements.insert(no.value)
            self.inOrder(no.right, value)
    
    def preOrder(self, no):
        if no is not None:
            print(no.value)
            self.elements.insert(no.value)
            self.preOrder(no.left)
            self.preOrder(no.right)

    def search(self,no, value):
        if no is None or no.value == value:
            return no
        if value >= no.value:
            return self.search(no.right, value)
        else:
            return self.search(no.left, value)
    
    
    #casos para fazer a remoção:
    #o nó não tem filhos - apenas remove o nó
    #o nó tem um filho - troca o nó de lugar com o filho e remove o nó
    #o nó tem dois filhos - dentre os elementos menores que o nó, encontre o maior e troque que lugar com ele. depois remova o nó
        
    def remove(self, pos, parent, value):
        if pos is None:  
            return pos
            
        elif value > pos.value:
            pos.right = self.remove(pos.right, pos, value)

        elif value < pos.value:
            pos.left = self.remove(pos.left, pos, value)
         # nessa parte o que estavamos procurando é igual a posição que estamos   
        else:

            if parent is not None:
                if pos.left is None and pos.right is None:
                #caso 1, onde o nó não tem filhos
                    if parent.right == pos:
                        parent.right = None
                        return None
                    else:
                        parent.left = None
                        return None 
                 #o nó tem alguns dos lados vazios, ou seja, tem apenas um filho      
                elif pos.right is None or pos.left is None:
                    if pos.right is not None:
                        child = pos.right
                    else:
                        child = pos.left
                    
                    if parent.right == pos:
                        parent.right = child
                    else:
                        parent.left = child
                    return child   
                 
                elif pos.right is not None and pos.left is not None:
                    smallBigNo = pos.right
                    while smallBigNo.left is not None:
                        smallBigNo = smallBigNo.left
                    pos.value = smallBigNo.value
                    #remover o duplicado começando por pos.right para evitar problemas
                    self.remove(pos.right, pos, pos.value)

                    
                    
                    


            else:
                
                #isso acontece quando precisamos deletar a raiz
                #repetir os mesmos casos de quantidade de filhos
                #prestar atenção nos argumentos das chamadas recurssivas
                if pos.left is None and pos.right is None:
                    pos = None
                elif pos.right is None or pos.left is None:
                    if pos.right is None:
                        self.root = pos.left
                        return pos.left
                    elif pos.left is None:
                        self.root = pos.right
                        return pos.right

                elif pos.right is not None and pos.left is not None:
                    smallBigNo = pos.right
                    while smallBigNo.left is not None:
                        smallBigNo = smallBigNo.left                    
                    pos.value = smallBigNo.value
        
                    self.remove(pos.right, pos, pos.value)

        
        return pos


                    






def main():
    lines = int(input())
    size = 0
    valores = input().split()
    for obj in valores:
        size += 1
    tree = Tree(size)    
        
    for i in valores:
        i = int(i)
        tree.insert( Node(i), tree.root)
    to_remove = input().split()
    stop = int(input())  
    tree.inOrder(tree.root, stop)
    tree.elements.showList(stop) 

    for i in to_remove:
        tree.remove(tree.root, None, int(i))
    print()
    tree.refresh()
    tree.inOrder(tree.root, stop)
    tree.elements.showList(stop)




if __name__ == '__main__':
    main()
