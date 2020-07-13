# -*- coding:utf-8 -*-
class Solution:

    def Fibonacci(self, n):
        # write code here        
        def fibs(k):
            
            if k == 1:
                return 1
            if k == 0:
                return 0
            
            return fibs(k-1) + fibs((k-2))
            
        return fibs(n)

    def fib(self, n):
        # write code here
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        n_0 = 0
        n_1 = 1
        res = 0
        for i in range(1, n):
            # print("1, ", n_0, n_1)
            res = n_0 + n_1
            n_0 = n_1
            n_1 = res
            # print("2, ", n_0, n_1)
            
        return res

print(Solution().fib(0))
print("==========================================")
print(Solution().fib(1))
print("==========================================")
print(Solution().fib(2))
print("==========================================")
print(Solution().fib(3))
print("==========================================")
print(Solution().fib(4))
print("==========================================")
print(Solution().fib(5))
print("==========================================")
print(Solution().fib(6))
print("==========================================")

print(Solution().fib(20))