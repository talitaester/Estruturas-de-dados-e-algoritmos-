import numpy as np

class No:
    def __init__(self, n):
        self.valor = n
        self.prox = None
    
    def show(self):
        return (f'{self.valor}')
    
class Lista:
    def __init__(self):
        self.head = None
    
    def insert_inicio(self, n):
        if self.head is None:
            self.head = n
        else:
            n.prox = self.head
            self.head = n
    
    def show(self):
        print("***Lista***")
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(f'{temp.show()}')
                temp = temp.prox

def main():
    l = Lista()
    l.show()
    l.insert_inicio(No(10))
    l.insert_inicio(No(20))
    l.insert_inicio(No(30))
    l.show()


if __name__ == '__main__':
    main()
