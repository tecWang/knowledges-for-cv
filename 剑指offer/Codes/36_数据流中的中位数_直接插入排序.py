# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
    
    def Insert(self, num):
        # write code here
        if self.arr == []:
            self.arr.append(int(num))
        else:
            # 使用插入排序优化算法性能
            k = len(self.arr) - 1
            while k >= 0:
                # print(int(num), self.arr[k], k)
                if int(num) < self.arr[k]:
                    k -= 1
                else:
                    self.arr.insert(k+1, int(num))
                    return
            
            # 比所有情况都小
            if k == -1:
                self.arr.insert(k+1, int(num))
            
        
    def GetMedian(self, data):
        # write code here
        if len(self.arr) == 1:
            return self.arr[0]
        
        elif len(self.arr) % 2 == 0:
            mid = (0 + len(self.arr) - 1) >> 1
            return (self.arr[mid] + self.arr[mid+1]) / 2.0
        else:
            return self.arr[(0 + len(self.arr) - 1) >> 1]

s = Solution()

while True:
    a = input()
    s.Insert(a)
    
    print(s.arr, s.GetMedian([]))