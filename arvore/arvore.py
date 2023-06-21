# código que implementa o tad árvore e realiza oprações de inserção, busca, etc. 
# a inserção aqui é feita da direita para a esquerda, considerando que um nível precisa ser preenchido
# inteiramente antes de começar a preencher outro nível.
# os valores das chaves não são levados em conta nessa inserção.
# a função main recebe um valor inteiro que indica N linhas que serão lidas, um vetor de elementos para adicionar na arvore
# e N-1 linhas com 2 elementos que vão ser buscados na árvore.
# Caso ambos sejam encontrados, ele deverá retornar a diferença de nível entre eles, caso somente um esteja na árvore,
# então retorna a altura do elemento, mas se ninguém estiver, retorna a altura da árvore


# classe tad filha que ajuda na operação de inserção
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, no):
        if self.first is None:
            self.first = no
            self.last = no
            self.size += 1
        else:
            self.last.prox = no
            self.last = no
            self.size += 1

    def remove(self):
        if self.first is not None:
            temp = self.first
            self.first = self.first.prox
            self.size -= 1
            return temp
    
#tad lista ajuda na operação de print dos valores
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


    def showList(self):
      for i in self.objList:
        if i is not None:
            print(i)
#classe node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.prox = None


class AVLTree:
    def __init__(self):
        self.root = None

#for god sakeeee
    def insert(self, value):
        #função para inserir um valor na arvore
        if self.root is None:
            self.root = Node(value)
            #se for vazia, adiciona na raiz
        else:
            #caso contrário, crie uma fila. o primeiro elemento da fila precisa ser o primeiro a ter seu left e right preeenchido
            queue = Queue()
            queue.push(self.root)
            while queue.first is not None:
                node = queue.remove()
                if node.left is None:
                    node.left = Node(value)
                    break
                elif node.right is None:
                    node.right = Node(value)
                    break
                else:
                    #caso o elemento que eu tirei ja tenha left e right preenchido, então olho cada no filho separadamente, adicionando-os na fila
                    #como o elemento a esquerda tem prioridade, adicioná-lo antes 
                    queue.push(node.left)
                    queue.push(node.right)

                #repetir tudo ate encontrar um nó que tenha uma posição livre 

    def preOrder(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def treeHeight(self, node):
        if node is None:
            return 0
        else:
            left_height = self.treeHeight(node.left)
            right_height = self.treeHeight(node.right)
            return max(left_height, right_height) + 1
        
    
    def findNodeHeight(self, node, value):
        #função para achar o maior caminho possivel de um nó ate uma folha
        if node is None:
            return -1

        if node.value == value:
            return self.nodeHeight(node)

        left_height = self.findNodeHeight(node.left, value)
        right_height = self.findNodeHeight(node.right, value)

        if left_height != -1:
            return left_height
        elif right_height != -1:
            return right_height
        else:
            return -1
        
    def noded_depth(self, node, value, depth):
        #função para achar o nível do nó em relação a raiz, ou seja, sua profundidade
        if node is None:
            return -1

        elif node.value == value:
            return depth

        left_height = self.noded_depth(node.left, value, depth+1)
        right_height = self.noded_depth(node.right, value, depth+1)

        if left_height != -1:
            return left_height
        elif right_height != -1:
            return right_height
        else:
            return -1



    def nodeHeight(self, node):
        #função que encontra um nó na arvore e calcula sua altura
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        if node.value == self.root.value:
            return self.treeHeight(self.root) -1
        right_height = self.nodeHeight(node.right) 
        left_height = self.nodeHeight(node.left) 

        return max(left_height, right_height) + 1

def main():
    tree =  AVLTree()
    lines = int(input())
    valores = input().split()
    for i in valores:
        i =  int(i)
        tree.insert(i)
    heights = listES(lines)
    #calcula a altura total da arvore e diminui 
    height = tree.treeHeight(tree.root) - 1
    #olha cada par de valor passado e avalia se eles estão na arvore e realiza as devidas operações
    for i in range(lines -1):
        x, y = input().split()
        x = int(x)
        y = int(y)
        height1 = tree.findNodeHeight(tree.root, x)
        height2 = tree.findNodeHeight(tree.root, y)
        if height1 == -1 and height2 == -1:
            heights.insert(height)
        elif height1 == -1:
            heights.insert(height2)
        elif height2 == -1:
            heights.insert(height1)
        else:
            depth1 = tree.noded_depth(tree.root, x, 0)
            depth2 = tree.noded_depth(tree.root, y, 0)
            gap = depth1 - depth2
            if gap < 0:
                gap = -gap
            heights.insert(gap)

    heights.showList()






if __name__ == '__main__':
    main()
