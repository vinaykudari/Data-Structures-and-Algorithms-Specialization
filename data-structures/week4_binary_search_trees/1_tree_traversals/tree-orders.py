# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class TreeOrders:
    def __init__(self):
        self.root = None
        self.inOrderList = []
        self.preOrderList = []
        self.postOrderList = []
        self.nodesOrder = []

    def read(self):
        self.n = int(input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, input().split())
            self.key[i] = TreeNode(a)
            self.left[i] = b
            self.right[i] = c

    def generateTree(self):
        self.root = self.key[0]
        leftIndex = self.left[0]
        rightIndex = self.right[0]
        if leftIndex != -1:
            self.root.left = self.key[leftIndex]
            self.nodesOrder.append(self.left[0])
        if rightIndex != -1:
            self.root.right = self.key[rightIndex]
            self.nodesOrder.append((self.right[0]))
        # print(f'root.val = {self.root.val}; root.left.val = {self.root.left.val}; root.right.val = {self.root.right.val}; ')
        i = 0
        while i < self.n -1:
            # print(f'finding self.key[self.nodesOrder[i]] : {self.key[self.nodesOrder[i]]}')
            node = self.key[self.nodesOrder[i]]
            leftIndex = self.left[self.nodesOrder[i]]
            rightIndex = self.right[self.nodesOrder[i]]
            if leftIndex != -1:
                node.left = self.key[leftIndex]
                # print(f'node={node.val}; node.left={node.left.val};')
                self.nodesOrder.append(leftIndex)
            if rightIndex != -1:
                node.right = self.key[rightIndex]
                # print(f'node={node.val}; node.right={node.right.val};')
                self.nodesOrder.append(rightIndex)
            i += 1

    def inOrder(self, root=None):
        if root is None:
            root = self.root
        if root.left:
            self.inOrder(root.left)
        self.inOrderList.append(root.val)
        if root.right:
            self.inOrder(root.right)

    def preOrder(self, root=None):
        if root is None:
            root = self.root
        self.preOrderList.append(root.val)
        if root.left:
            self.preOrder(root.left)
        if root.right:
            self.preOrder(root.right)

    def postOrder(self, root=None):
        if root is None:
            root = self.root
        if root.left:
            self.postOrder(root.left)
        if root.right:
            self.postOrder(root.right)
        self.postOrderList.append(root.val)


def main():
    tree = TreeOrders()
    tree.read()
    tree.generateTree()
    tree.inOrder()
    tree.preOrder()
    tree.postOrder()
    print(" ".join(str(x) for x in tree.inOrderList))
    print(" ".join(str(x) for x in tree.preOrderList))
    print(" ".join(str(x) for x in tree.postOrderList))


threading.Thread(target=main).start()
