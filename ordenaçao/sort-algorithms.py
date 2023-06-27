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

    def delList(self):
        i = 0
        while i < self.size:
            self.objList[i] = None
            i += 1
        self.size = 0

    def showList(self, limit = list.size):
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



def main():
    lines = int(input())
    max_iterations = int(input())
    unsorted_list = listES(lines - 1) 
    for _ in range(lines - 1):
        value = int(input())
        unsorted_list.insert(value)

    unsorted_list.insertion(max_iterations)
    #if u want to see the whole list u dont need to use a limit
    unsorted_list.showList(max_iterations)


if __name__ == '__main__':
    main()