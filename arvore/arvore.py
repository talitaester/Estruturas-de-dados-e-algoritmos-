
from collections import deque
class Queue:
    def __init__(self):
        self.first = None
        self.size = 0

    def push(self, value):
        no = Node(value)
        if self.first is None:
            self.first = no
            self.size += 1
        else:
            temp = self.first
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = no
            size += 1

    def pop(self):
        if self.first is not None:
            temp = self.first
            self.first = self.first.prox
            self.size -= 1
            return temp
    
    def isnt_empty(self):
           return self.size != 0

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.prox = None


class AVLTree:
    def __init__(self):
        self.root = None

#for god sake
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            queue = deque([self.root])
            while queue:
                node = queue.popleft()
                if node.left is None:
                    node.left = Node(key)
                    break
                elif node.right is None:
                    node.right = Node(key)
                    break
                else:
                    queue.append(node.left)
                    queue.append(node.right)

    def print_preorder(self, node):
        if node is not None:
            print(node.key, end=' ')
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def calculate_tree_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.calculate_tree_height(node.left)
            right_height = self.calculate_tree_height(node.right)
            return max(left_height, right_height) + 1
        
    
    def find_element_height_recursive(self, node, key):
        if node is None:
            return -1

        if node.key == key:
            return self.calculate_element_height(node)

        left_height = self.find_element_height_recursive(node.left, key)
        right_height = self.find_element_height_recursive(node.right, key)

        if left_height != -1:
            return left_height
        elif right_height != -1:
            return right_height
        else:
            return -1
        
    def noded_depth(self, node, key, depth):
        if node is None:
            return -1

        elif node.key == key:
            return depth

        left_height = self.noded_depth(node.left, key, depth+1)
        right_height = self.noded_depth(node.right, key, depth+1)

        if left_height != -1:
            return left_height
        elif right_height != -1:
            return right_height
        else:
            return -1



    def calculate_element_height(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        if node.key == self.root.key:
            return self.calculate_tree_height(self.root) -1

        left_height = self.calculate_element_height(node.left) 
        right_height = self.calculate_element_height(node.right) 

        return max(left_height, right_height) + 1

def main():
    tree =  AVLTree()
    lines = int(input())
    valores = input().split()
    heights = []
    valores = [int(x) for x in valores]
    for i in valores:
        tree.insert(i)
    height = tree.calculate_tree_height(tree.root) - 1
    for i in range(lines -1):
        x, y = input().split()
        x = int(x)
        y = int(y)
        height1 = tree.find_element_height_recursive(tree.root, x)
        height2 = tree.find_element_height_recursive(tree.root, y)
        if height1 == -1 and height2 == -1:
            heights.append(height)
        elif height1 == -1:
            heights.append(height2)
        elif height2 == -1:
            heights.append(height1)
        else:
            depth1 = tree.noded_depth(tree.root, x, 0)
            depth2 = tree.noded_depth(tree.root, y, 0)
            gap = depth1 - depth2
            if gap < 0:
                gap = -gap
            heights.append(gap)

    print(*heights)
    # tree.print_preorder(tree.root)
    # print('')
    # print(height)





if __name__ == '__main__':
    main()
