# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        
        if s == "0":
            return 0
        
        temp = "+"
        if s[0] == "+" or s[0] == "-":
            temp = s[0]
            s = s[1:]
        
        res = []
        for val in s:
            if res:
                res = [10*x for x in res]
            if "0" <= val <= "9":
                res.append(int(val))
            else:
                return 0
        
        if temp == "+":
            return sum(res)
        else:
            return -1*sum(res)

print(Solution().StrToInt("+2147483647"))
print(Solution().StrToInt("1a33"))
print(Solution().StrToInt("123"))