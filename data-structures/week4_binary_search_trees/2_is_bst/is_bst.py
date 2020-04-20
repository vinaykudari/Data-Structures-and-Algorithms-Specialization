# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.leftBound = ()
        self.rightBound = ()


class TreeOrders:
    def __init__(self):
        self.root = None
        self.nodesOrder = []
        self.key = []
        self.n = None
        self.left = []
        self.right = []

    def read(self):
        self.n = int(input())
        self.key = [TreeNode() for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, input().split())
            self.key[i].val = a
            self.left[i] = b
            self.right[i] = c

    def find(self, data, root=None):
        if not root:
            root = self.root
        if data == root.val:
            return True, root
        elif data < root.val:
            # print(f'data({data}) < root({root.val})')
            if root.left:
                return self.find(data, root.left)
            else:
                return False, root
        elif data > root.val:
            # print(f'data({data}) > root({root.val})')
            if root.right:
                return self.find(data, root.right)
            else:
                return False, root

    def isBinaryTree(self):
        if self.n == 0:
            return True
        self.root = self.key[0]
        leftIndex = self.left[0]
        rightIndex = self.right[0]
        if leftIndex != -1:
            leftNode = self.key[leftIndex]
            if leftNode.val > self.root.val:
                return False
            self.root.left = leftNode
            leftNode.leftBound = float('-inf'), leftNode.val
            leftNode.rightBound = leftNode.val, self.root.val
            self.nodesOrder.append(leftIndex)
        if rightIndex != -1:
            rightNode = self.key[rightIndex]
            if rightNode.val < self.root.val:
                return False
            self.root.right = rightNode
            rightNode.leftBound = self.root.val, rightNode.val
            rightNode.rightBound = rightNode.val, float('inf')
            self.nodesOrder.append(rightIndex)
        i = 0
        while i < self.n - 1:
            node = self.key[self.nodesOrder[i]]
            leftIndex = self.left[self.nodesOrder[i]]
            rightIndex = self.right[self.nodesOrder[i]]
            # print(f'node = {node.val}; ')
            if leftIndex != -1:
                leftNode = self.key[leftIndex]
                # print(f'node = {node.val}; leftNode = {leftNode.val}; Bounds = {node.leftBound[0], node.leftBound[1]}')
                if node.leftBound[0] > leftNode.val or leftNode.val > node.leftBound[1]:
                    return False
                node.left = leftNode
                leftNode.leftBound = float('-inf'), leftNode.val
                leftNode.rightBound = leftNode.val, node.leftBound[1]
                self.nodesOrder.append(leftIndex)
            if rightIndex != -1:
                rightNode = self.key[rightIndex]
                # print(f'node = {node.val}; rightNode = {rightNode.val}; Bounds = {node.rightBound[0], node.rightBound[1]}')
                if node.rightBound[0] > rightNode.val or rightNode.val > node.rightBound[1]:
                    return False
                node.right = rightNode
                rightNode.leftBound = node.rightBound[0], rightNode.val
                rightNode.rightBound = rightNode.val, float('inf')
                self.nodesOrder.append(rightIndex)
            i += 1
        return True


def main():
    tree = TreeOrders()
    tree.read()
    flag = tree.isBinaryTree()

    if flag:
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
