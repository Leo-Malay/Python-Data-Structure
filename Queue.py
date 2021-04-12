#
#   Implemented: Queue
#   Author: Malay Bhavsar
#   Date: 12-04-2021
#   Version: 1.0
#


class Node:
    def __init__(self, data: any = None) -> None:
        self.data = data
        self.next = None


class PNode:
    def __init__(self, data: any = None, priority: list = None) -> None:
        self.priority = priority
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = Node()
        self.back = self.front

    def insertNode(self, data: any = None) -> None:
        newNode = Node(data)
        self.back.next = newNode
        self.back = self.back.next

    def removeNode(self) -> None:
        self.front = self.front.next

    def getNode(self) -> any:
        return self.front.data

    def listNode(self) -> list:
        temp = self.front
        res = []
        while temp.next != None:
            res.append(temp.data)
            temp = temp.next
        res.append(temp.data)
        return res


class DeQueue:
    def __init__(self):
        self.front = Node()
        self.back = self.front

    def insertNodeFront(self, data: any = None) -> None:
        newNode = Node(data)
        newNode.next = self.front
        self.front = newNode

    def insertNodeBack(self, data: any = None) -> None:
        newNode = Node(data)
        self.back.next = newNode
        self.back = self.back.next

    def removeNodeFront(self) -> None:
        self.front = self.front.next

    def removeNodeBack(self) -> None:
        temp = self.front
        while temp.next != self.back:
            temp = temp.next
        self.back = temp
        self.back.next = None

    def listNode(self) -> list:
        temp = self.front
        res = []
        while temp.next != None:
            res.append(temp.data)
            temp = temp.next
        res.append(temp.data)
        return res
