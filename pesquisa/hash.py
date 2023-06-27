
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
            while temp is not None:
                print(temp.showNode(), end=" ")
                temp = temp.prox 

    def Insert(self, no):
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
        return
    
    def insertX(self, index, value):
        if self.objList[index] is None:
            data = ListEnc()
            data.Insert(value)
            self.objList[index] = data
        else:
            data = self.objList[index] 
            data.Insert(value)


    def showList(self, limit):
        j = 0
        for i in self.objList[:self.size]:
            if j < limit:
                print(i, end=" ") 
                j += 1
        return

class Hash:
    def __init__(self, hash_size) -> None:
        self.hash_size = hash_size
        self.table =  listES(hash_size)

    def position(self, word):
        asciiSUM = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for char in word:
            i = 1
            for char2 in alphabet:
                if char2 == char:
                    break
                else:
                    i += 1
            asciiSUM += i
        index = asciiSUM % self.hash_size
        return index

    def insert(self, word):
        index =  self.position(word) 
        self.table.insertX(index, word)
    
    def search(self, id):
        data = self.table.objList[id] 
        return data

def main():
    lines = int(input())
    hash_size = int(input())
    my_hash = Hash(hash_size)
    searchID =int(input())
    for i in range(lines-2):
        word = input().strip()
        my_hash.insert(word)
    data = my_hash.search(searchID)
    data.show()


if __name__ == '__main__':
    main()


