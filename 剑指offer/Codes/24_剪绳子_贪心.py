# -*- coding:utf-8 -*-
import math
class Solution:
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 1
        elif number == 3:
            return 2
        
        m = math.ceil(math.sqrt(number))
        n_slices = number // m
        print(m, n_slices)
        if number - m*n_slices > 0:
            return m**n_slices*(number - m*n_slices)
        else:
            return m**n_slices

print(Solution().cutRope(3))
print(Solution().cutRope(4))
print(Solution().cutRope(8))