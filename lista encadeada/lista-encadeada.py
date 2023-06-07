
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
    def delList(self):
        self.head = None
    #    
    #def cicleDetector(self):
    #    temp = self.head
    #    print('im hereee')
    #    for i in range(self.size -1):
    #        temp = temp.prox
    #    if temp.prox == None:
    #        print("no cicle")
    #    else:
    #        print("cicle detected")
#
    def createcicle(self, value):
        temp = self.head
        temp2 = self.head
        while True:
            if temp.value == value:
                temp2 = temp  
            if temp.prox is not None:
                temp = temp.prox
            else:
                temp.prox = temp2
                break

        

    def cicleDetector(self):
        temp = self.head
        temp2 = self.head
        while True:
            if temp2.prox is None:
                print("Sem Ciclo")
                break
            elif temp2.prox.prox is None:
                print("Sem Ciclo")
                break
            else:
                temp2 = temp2.prox.prox                   

            if temp.prox is None:
                print("Sem Ciclo")
                break                
            else:
                temp = temp.prox
            if temp == temp2:
                print("Ciclo")
                break





def main():
    testList = ListEnc()
    size = int(input())
    list = input() #read input as as str 
    values = list.split()
    values = "".join(values)
    for i in range(size -1):
        
        if i < (size -2):
            curr, prox =  input().split()
            testList.insert(curr)
        else :
            curr, prox =  input().split()
            testList.insert(curr)
            if prox != values[size-1]:
                testList.createcicle(prox)

    testList.cicleDetector()

if __name__ == '__main__':
    main()

