import numpy as np

class Element:
    def __init__(self, value):
        self.value = value 
        self.prox = None

    def showNode(self):
        return (self.value)

class ListEnc:
    def __init__(self): 
        self.head = None
        self.size = 0
    
    def show(self):
        if self.head is not None:
            temp = self.head
            print('**LISTA**')
            while temp is not None:
                print(temp.showNode())
                temp = temp.prox


    
    def insert(self, no):
        node = Element(no)
        if self.head is None:
            self.head = node
            self.size += 1
        else:
            node.prox = self.head
            self.head = node
            self.size += 1

    def endInsert(self, no):
        node = Element(no)
        if self.head is not None:
            current_node = self.head
            while True:               
                if current_node.prox is not None:
                    current_node = current_node.prox
        
                else:
                    current_node.prox = node
                    self.size += 1
                    break
        else:
            self.head = node

    def insertInPosition(self, no, pos):
        
        node = Element(no)
        temp = self.head
        past = None
        for i in range(pos):
            past = temp
            temp = temp.prox
            if i == pos-1:
                print("im here")
                past.prox = node
                node.prox = temp


def main():
    testList = ListEnc()
    testList.insert(1)
    testList.insert(2)
    testList.insert(3)
    testList.endInsert(8)
    testList.insertInPosition(7, 2)
    testList.show()

if __name__ == '__main__':
    main()

