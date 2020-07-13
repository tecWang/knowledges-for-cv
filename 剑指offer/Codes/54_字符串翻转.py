# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        if not s:
            return s

        res = s.split()
        if len(res) == 0:
            return s

        out = ""
        while res:
            out += res[-1] + " "
            res.pop()
        return out.strip()

print(Solution().ReverseSentence(" "))
print(Solution().ReverseSentence("I am a student."))
print(Solution().ReverseSentence("Wonderful"))