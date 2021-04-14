#
#   Implemented: Tree
#   Author: Malay Bhavsar
#   Date: 14-04-2021
#   Version: 1.0
#


class Node:
    def __init__(self, data: any = None) -> None:
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self, data: any = None) -> None:
        self.root = Node(data)

    def getRoot(self):
        return self.root

    def insertNode(self, data: any = None):
        newNode = Node(data)
        root = self.getRoot()
        while root != None:
            if data >= root.data:
                if root.right != None:
                    root = root.right
                else:
                    root.right = newNode
                    break
            elif data < root.data:
                if root.left != None:
                    root = root.left
                else:
                    root.left = newNode
                    break

    def inOrderNode(self) -> list:
        res = []

        def traverse(temp):
            if temp == None:
                return
            traverse(temp.left)
            res.append(temp.data)
            traverse(temp.right)
            return
        traverse(self.getRoot())
        return res

    def preOrderNode(self) -> list:
        res = []

        def traverse(temp):
            if temp == None:
                return
            res.append(temp.data)
            traverse(temp.left)
            traverse(temp.right)
            return
        traverse(self.getRoot())
        return res

    def postOrderNode(self) -> list:
        res = []

        def traverse(temp):
            if temp == None:
                return
            traverse(temp.left)
            traverse(temp.right)
            res.append(temp.data)
            return
        traverse(self.getRoot())
        return res
