# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while(num2 != 0):
            s1 = num1^num2
            s2 = (num1&num2)<<1
            num1 = s1 & 0xFFFFFFFF
            num2 = s2
            print(s1, s2, num1, num2)
        return num1  if num1 >> 31 == 0 else num1 - 4294967296

print(Solution().Add(5, 7))
print(Solution().Add(-5,7))


