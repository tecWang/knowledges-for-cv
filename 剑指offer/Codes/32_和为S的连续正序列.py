# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # 连续正序列 = 差为1的等差递增数列
        # tsum = 100 = (a+b)*n/2
        # (a+b)*n = 200
        # n的条件，能被200整除,且n>=2,并且n<=(a+b)
        res = []
        tsum = tsum*2
        n = tsum
        while n >= 2:
            mod_n = tsum % n
            if mod_n == 0:
                a_b = tsum // n

                if (a_b - (n - 1)) % 2 != 0:
                    n -= 1
                    continue
                    
                a = (a_b - (n - 1)) // 2
                b = a + n - 1

                if b > 100:
                    n -= 1
                    continue
                
                if a <= 0:
                    n -= 1
                    continue
                
                s = []
                for k in range(a, b+1):
                    s.append(k)
                print("tsum, n, s, a, b:", tsum, n, s, a, b)
                res.append(s)
            n -= 1
        return res

print(Solution().FindContinuousSequence(100))
print(Solution().FindContinuousSequence(1))
print(Solution().FindContinuousSequence(4))