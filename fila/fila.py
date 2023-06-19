
class Element:
    def __init__(self, value, ID):
        self.value = int(value)
        self.ID = int(ID)
        self.prox = None

    def showNodeID(self):
        return (self.ID)

    def showNodevalue(self):
        return (self.value)
    

class queue:
    def __init__(self):
        self.first = None

    def show(self):
        if self.first is not None:
            temp = self.first
            while temp is not None:
                print(temp.showNodeID(), end=' ')
                temp = temp.prox
            temp = self.first
            print()
            while temp is not None:
                print(temp.showNodevalue(), end=' ')
                temp = temp.prox           
    
    def append(self, value, ID):
        #esse append cria um elemento nó com os valores passados
        no = Element(value, ID)
        if self.first is None:
            self.first = no
        else:
            temp = self.first
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = no

    
 


    def remove(self):
        if self.first is not None:
            self.first = self.first.prox
        
    def sistemaOperacional(self, maxUP, quantum):

        if self.first is not None:
            temp = self.first

            while (maxUP > 0):

                if (temp.value <= quantum) and (temp.value <= maxUP):
                    maxUP -= temp.value
                    temp.value = 0

                else:
                    if maxUP >= quantum:
                        maxUP -= quantum
                        temp.value -= quantum
                    else:
                        temp.value -= maxUP 
                        maxUP = 0
                self.remove()
                
                if temp.value > 0:
                    self.append(temp.value, temp.ID)

                if temp.prox is not None:
                    temp =  temp.prox
                
            


            

                


def main():
    Queue = queue()
    #reading data 
    lines = int(input())
    lines -= 1
    quantum, maxUP = input().split()
    maxUP = int(maxUP)
    quantum = int(quantum)
    ids = input().split()
    values = input().split()
    j = 0
    for i in values:
        Queue.append(i, ids[j])
        j+=1
    #finished reading data
    Queue.sistemaOperacional(maxUP, quantum)
    Queue.show()




if __name__ == '__main__':
    main()
    

    

