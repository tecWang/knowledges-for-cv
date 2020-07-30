# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        
        if tinput == []:
            return []

        import heapq
        heapq.heapify(tinput)
        res = []
        for i in range(k):
            res.append(heapq.heappop(tinput))
        return res

print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))