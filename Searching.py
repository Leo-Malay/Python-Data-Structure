#
#   Implemented: Searching Algorithms
#   Author: Malay Bhavsar
#   Date: 15-04-2021
#   Version: 1.0
#


class Searching:
    def __init__(self, data_arr: list) -> None:
        self.arr = data_arr
        self.length = len(self.arr)

    def linearSearch(self, val: any) -> int:
        for i in range(self.length):
            if val == self.arr[i]:
                return i
        return -1

    def binarySearch(self, val: any) -> int:
        low = 0
        high = self.length
        while low <= high:
            mid = (low + high)//2
            if val == self.arr[mid]:
                return mid
            elif val > self.arr[mid]:
                low = mid
            else:
                high = mid
        return -1
