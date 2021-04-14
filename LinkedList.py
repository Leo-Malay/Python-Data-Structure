#
#   Implemented: Linked List
#   Author: Malay Bhavsar
#   Date: 11-04-2021
#   Version: 1.0
#


class SNode:
    def __init__(self, data: any = None) -> None:
        self.data = data
        self.next = None


class DNode:
    def __init__(self, data: any = None) -> None:
        self.data = data
        self.next = None
        self.prev = None


class SingleLinkedList:
    def __init__(self):
        self.head = SNode()
        self.length = 0

    def getHead(self):
        return self.head

    def getLength(self):
        return self.length

    def isEmpty(self):
        head = self.getHead()
        return head.next == None

    def create(self, arr: list) -> None:
        self.head = SNode()
        head = self.getHead()
        for ele in arr:
            head.next = SNode(ele)
            head = head.next

    def indexOfNode(self, data: any = None) -> int:
        if self.isEmpty():
            return None
        head = self.getHead()
        count = 0
        while head.next != None:
            if data == head.data:
                return count
            count += 1
            head = head.next
        return None

    def valueOfNode(self, index: int = 0) -> any:
        if self.isEmpty() or index > self.length:
            return None
        count = 0
        head = self.getHead()
        while count < index:
            head = head.next
            count += 1
        return head.data

    def insertNode(self, data: any = None) -> None:
        head = self.getHead()
        while head.next != None:
            head = head.next
        head.next = SNode(data)
        self.length += 1

    def insertSortedNode(self, data: any = None) -> None:
        newNode = SNode(data)
        self.length += 1
        head = self.getHead()
        if head.next == None:
            head.next = newNode
        else:
            temp = head.next
            while data > temp.data:
                temp = temp.next
                head = head.next
                if temp == None:
                    head.next = newNode
                    return
            head.next = newNode
            newNode.next = temp

    def updateNode(self, index: int = -1, data: any = None) -> None:
        if index > self.length or index == -1:
            return
        count = 0
        head = self.getHead()
        while count != index:
            head = head.next
            count += 1
        head.data = data

    def removeNode(self, index: int = None, total: int = 1) -> None:
        if self.isEmpty() or index > self.length:
            return
        count = 0
        head = self.getHead()
        while count < index - 1:
            head = head.next
            count += 1
        temp = head
        self.length -= total
        while total != 0:
            temp = temp.next
            total -= 1
        head.next = temp.next

    def listNode(self) -> list:
        if self.isEmpty():
            return []
        head = self.getHead()
        result = []
        head = head.next
        while head.next != None:
            result.append(head.data)
            head = head.next
        result.append(head.data)
        return result

    def flushNode(self, index: int = 0) -> None:
        if index > self.length:
            return
        count = 0
        head = self.getHead()
        while count < index:
            head = head.next
            count += 1
        head.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = DNode()
        self.length = 0

    def getHead(self):
        return self.head

    def getLength(self):
        return self.length

    def isEmpty(self):
        head = self.getHead()
        return head.next == None and head.prev == None

    def create(self, arr: list) -> None:
        self.head = DNode()
        head = self.getHead()
        for ele in arr:
            newNode = DNode(ele)
            head.next = newNode
            newNode.prev = head
            head = head.next

    def indexOfNode(self, data: any = None) -> int:
        if self.isEmpty():
            return None
        head = self.getHead()
        count = 0
        while head.next != None:
            if data == head.data:
                return count
            count += 1
            head = head.next
        return None

    def valueOfNode(self, index: int = 0) -> any:
        if self.isEmpty() or index > self.length:
            return None
        count = 0
        head = self.getHead()
        while count < index:
            head = head.next
            count += 1
        return head.data

    def insertNodeFront(self, data: any = None) -> None:
        self.length += 1
        head = self.getHead()
        temp = DNode(data)
        temp2 = head.next
        temp.prev = head
        temp.next = temp2
        head.next = temp
        temp2.prev = temp

    def insertNodeBack(self, data: any = None) -> None:
        self.length += 1
        head = self.getHead()
        while head.next != None:
            head = head.next
        head.next = SNode(data)
        temp = head
        temp = temp.next
        temp.prev = head
        self.length += 1

    def updateNode(self, index: int = -1, data: any = None) -> None:
        if index > self.length or index == -1:
            return
        count = 0
        head = self.getHead()
        while count != index:
            head = head.next
            count += 1
        head.data = data

    def removeNode(self, index: int, total: int = 1):
        if self.isEmpty() or index > self.length:
            return
        count = 0
        head = self.getHead()
        while count < index - 1:
            head = head.next
            count += 1
        temp = head
        self.length -= total
        while total != 0:
            temp = temp.next
            total -= 1
        head.next = temp.next
        temp = temp.next
        temp.prev = head

    def listNodeFront(self) -> list:
        if self.isEmpty():
            return []
        head = self.getHead()
        result = []
        head = head.next
        while head.next != None:
            result.append(head.data)
            head = head.next
        result.append(head.data)
        return result

    def listNodeBack(self) -> list:
        if self.isEmpty():
            return []
        head = self.getHead()
        while head.next != None:
            head = head.next
        result = []
        while head.prev != None:
            result.append(head.data)
            head = head.prev
        return result
