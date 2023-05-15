

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
                 
                 

    def insertX(self, position, value):
       obj = value
       iter = self.size - position
       if self.size < self.max:
          for i in range(self.size, position -1, 1):
            self.objList[i] = self.objList[i+1]
          self.objList[position +1] = obj

             



    def showList(self):
      for i in self.objList:
        print(i)
    
     
def main():
 #end = 0
  list_size = int(input("digite o tamanho da lista "))
  testList = listES(list_size)
 #while end == 0:
 #  m =  int(input("digite um valor para inserir "))
 #  if testList.size >=list_size:
 #     print("sua lista atingiu o tamanho maximo :(")
 #  else:
 #     testList.insert(m)
 #     print(testList)
 #  end = int(input("0 para continuar e 1 para encerrar "))
  testList.insert(1)
  testList.insert(2)
  testList.insert(3)
  testList.insert(4)
  testList.insert(5)
  testList.insert(6)
  testList.insertX(3, 9)
  testList.showList()



if __name__ == '__main__':
    main()
    