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
        else:
            pass



    def delList(self):
        i = 0
        while i < self.size:
            self.objList[i] = None
            i += 1
        self.size = 0

    def showList(self, limit):
        j = 0
        for i in self.objList[:self.size]:
            if j < limit:
                print(i, end=" ") 
                j += 1

    def selection(self, limit):
        for i in range(limit):
            minIndex = i
            for j in range(i + 1, self.size):
                if self.objList[j] < self.objList[minIndex]:
                    minIndex = j
            self.objList[i], self.objList[minIndex] = self.objList[minIndex], self.objList[i]
        return self
    


    def insertion(self, limit):
        for i in range(1, limit):
            currentId = i
            while currentId > 0 and self.objList[currentId-1] > self.objList[currentId]:
                self.objList[currentId-1], self.objList[currentId] = self.objList[currentId], self.objList[currentId-1]
                currentId -= 1
        return self
    
    def bubble(self, limit):
        for i in range(limit):
            id1 = 0
            id2 = id1 + 1
            while id2 < self.size:
                if self.objList[id2] < self.objList[id1]:
                    self.objList[id2], self.objList[id1] = self.objList[id1], self.objList[id2]
                id1 += 1
                id2 += 1
        return self
    
def quicksort(myList, pivoId):
    if myList.size <= 1:
        return myList
    else:
        pivo = myList.objList[pivoId]
        
        leftList = listES(myList.max)
        rightList = listES(myList.max)

        for i in range(myList.size):
            if myList.objList[i] is not None:
                if myList.objList[i] > pivo:
                    rightList.insert(myList.objList[i])
                elif myList.objList[i] < pivo :
                    leftList.insert(myList.objList[i])

        leftList = quicksort(leftList, 0)
        rightList = quicksort(rightList, 0)

        sortedList = listES(myList.max + 2)
        for i in range(leftList.size):
            sortedList.insert(leftList.objList[i])
        sortedList.insert(pivo)
        for j in range(rightList.size):
            sortedList.insert(rightList.objList[j])

        return sortedList
    
def twopvs(myList, pivoId):
    pivoList = listES(myList.max + 2)
    pivo  = myList.objList[pivoId]
    for i in range(myList.max):
        if myList.objList[i] < pivo:
            pivoList.insert(myList.objList[i])
            break
    for i in range(myList.max):
        if myList.objList[i] > pivo:
            pivoList.insert(myList.objList[i])
            break
    return pivoList


    


                

            







def main():
    lines = int(input())
    pivoId = int(input())
    unsorted_list = listES(lines - 1) 
    for _ in range(lines - 1):
        value = int(input())
        unsorted_list.insert(value)

    sortedList = quicksort(unsorted_list, pivoId)

    pivlist =  twopvs(unsorted_list, pivoId)
    pivlist.showList(2)
    sortedList.showList(unsorted_list.size)



if __name__ == '__main__':
    main()