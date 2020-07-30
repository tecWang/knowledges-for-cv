# -*- coding:utf-8 -*-
import heapq

class Solution:
    def __init__(self):
        self.arr = []
        self.maxq = []   # 大根堆 
        self.minq = []   # 小根堆
    
    def Insert(self, num):
        # 在插入的时候维护两个堆，一个小根堆，一个大根堆
        heapq.heappush(self.minq, int(num))

        # 小根堆的最小元素插入大根堆
        # 这一步很重要，可以保证数据的重新排序
        val = heapq.heappop(self.minq)
        heapq.heappush(self.maxq, -val)
        
        # 保证两个堆的长度相差不超过1
        if abs(len(self.minq) - len(self.maxq)) > 1:
            val = heapq.heappop(self.maxq)
            heapq.heappush(self.minq, -val)

        # print("minq, maxq", [self.minq[index] for index in range(len(self.minq))], 
                            # [self.maxq[index] for index in range(len(self.maxq))])

        
    def GetMedian(self, data):
        if len(self.maxq) == len(self.minq):
            return (-self.maxq[0] + self.minq[0]) / 2.0
        else:
            return -self.maxq[0]


# 5,2,3,4,1,6,7,0,8
s = Solution()
while True:
    s.Insert(input())
    print("mean", s.GetMedian([]))
