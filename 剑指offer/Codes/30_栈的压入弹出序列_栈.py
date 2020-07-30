# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        
        stack = []
        stack.append(pushV.pop(0))
        print(stack)

        cnt = 0
        n = len(pushV)
        while stack and cnt <= n:

            while stack and stack[-1] == popV[0]:
                print(stack, popV)
                stack.pop()
                popV.pop(0)

            print(stack, popV)
            if pushV:
                stack.append(pushV.pop(0))
        
            cnt += 1

        print(stack, popV)
        if stack and stack[-1] != popV[0]:
            return False
        else:
            return True

print(Solution().IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))
print(Solution().IsPopOrder([1,2,3,4,5],[4,3,5,1,2]))