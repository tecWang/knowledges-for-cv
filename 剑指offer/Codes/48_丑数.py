# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        if index == 1:
            return 1
        ugly = [1]
        index_two = 0
        index_three = 0
        index_five = 0
        if index == 1:
            return ugly
        
        for i in range(1, index):
            new_ugly = min(ugly[index_two]*2, ugly[index_three]*3, ugly[index_five]*5)
            ugly.append(new_ugly)
            if new_ugly % 2 == 0:
                index_two += 1
            if new_ugly % 3 == 0:
                index_three += 1
            if new_ugly % 5 == 0:
                index_five += 1
        return ugly[-1]

print(Solution().GetUglyNumber_Solution(6))