class listES:
    def __init__(self, max):
        self.size = 0
        self.max = max
        self.objList = [None] * max


    def insert(self, obj):
        if self.size < self.max:
          self.objList[self.size] = obj
          self.size += 1

    def __str__(self):
      return str(self.objList[:self.size])
     
def main():
  end = 0
  list_size = int(input("digite o tamanho da lista "))
  testList = listES(list_size)
  while end == 0:
    m =  int(input("digite um valor para inserir "))
    if testList.size >=list_size:
       print("sua lista atingiu o tamanho maximo :(")
    else:
       testList.insert(m)
       print(testList)
    end = int(input("0 para continuar e 1 para encerrar "))
  print(testList)


if __name__ == '__main__':
    main()
    