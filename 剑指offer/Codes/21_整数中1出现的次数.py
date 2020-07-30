# -*- coding:utf-8 -*-
import re
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = ""
        for i in range(1, n):
            res += str(i)
        print(res, re.findall("1", res))
        return len(re.findall("1", res))

print(Solution().NumberOf1Between1AndN_Solution(10))
print(Solution().NumberOf1Between1AndN_Solution(1))