#
#   Implemented: Sorting Algorithms
#   Author: Malay Bhavsar
#   Date: 15-04-2021
#   Version: 1.0
#


class Sorting:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def bubbleSort(self):
        arr = [x for x in self.arr]
        isSorted = False
        while isSorted == False:
            isSorted = True
            for i in range(self.length - 1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i + 1], arr[i]
                    isSorted = False
        return arr

    def selectionSort(self):
        arr = [x for x in self.arr]
        for i in range(self.length-1):
            index = arr.index(min(arr[i:]))
            arr[i], arr[index] = arr[index], arr[i]
        return arr

    def insertionSort(self):
        arr = [self.arr[0]]
        for ele in self.arr[1:]:
            i = 0
            while arr[i] < ele:
                i += 1
                if i >= len(arr):
                    break
            arr.insert(i, ele)
        return arr
