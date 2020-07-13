# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        
        if n == 1:
            return 0
        
        stack = [i for i in range(n)]
        index = 0        
        while len(stack) > 1:
            index = (index + (m-1)) % len(stack)
            # print("stack", stack, "index", index)
            stack.pop(index)
        
        return stack[0]

print(Solution().LastRemaining_Solution(5, 3))
