class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Função da minha solução "insert" abaixo. O resto já estava implementado.
    def insert(self, val):
        # Enter your code here
        if self.root is None:
            self.root = Node(val)
            return

        atual = self.root
        while True:
            if val < atual.info:
                if atual.left is None:
                    atual.left = Node(val)
                    break
                atual = atual.left
            elif val > atual.info:
                if atual.right is None:
                    atual.right = Node(val)
                    break
                atual = atual.right
            else:
                break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
