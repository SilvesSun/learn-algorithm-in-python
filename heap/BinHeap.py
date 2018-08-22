# coding:utf-8
__date__ = '2018/6/19 12:29'


def less(e1, e2):
    return True if e1 <= e2 else False


class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def swim(self, i):
        while i // 2 > 0:
            if less(self.heapList[i], self.heapList[i//2]):
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.swim(self.currentSize)

    def sink(self, i):
        while i*2 <= self.currentSize:
            mc = self.minChild(i)
            if less(self.heapList[mc], self.heapList[i]):
                self.heapList[mc], self.heapList[i] = self.heapList[i], self.heapList[mc]

            i = mc

    def minChild(self, i):
        # only contains left child
        if less(self.currentSize, i*2+1):
            return i*2

        else:
            if less(self.heapList[i*2], self.heapList[i*2+1]):
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heapList[1]  # get the root value
        self.heapList[1] = self.heapList[self.currentSize]  # use the last node as current root
        self.heapList.pop()
        self.sink(1)
        return retval

