import heapq

class MedianFinder:

    def __init__(self):
        self.lowerHeap = []
        self.upperHeap = []

        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowerHeap, -num)
        if self.upperHeap and self.upperHeap[0] < -self.lowerHeap[0]:
            heapq.heappush(self.upperHeap, -heapq.heappop(self.lowerHeap))
        lowerLen = len(self.lowerHeap)
        upperLen = len(self.upperHeap)

        if lowerLen - upperLen > 1:
            heapq.heappush(self.upperHeap, -heapq.heappop(self.lowerHeap))

        elif upperLen - lowerLen > 1:
            heapq.heappush(self.lowerHeap, -heapq.heappop(self.upperHeap))





        

    def findMedian(self) -> float:
        lowerLen = len(self.lowerHeap)
        upperLen = len(self.upperHeap)
        if lowerLen > upperLen:
            return -self.lowerHeap[0]
        elif upperLen > lowerLen:
            return self.upperHeap[0]
        else:
            return 0.5*(-self.lowerHeap[0] + self.upperHeap[0])
        
        