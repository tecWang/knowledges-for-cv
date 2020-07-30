# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack  = []
        self.queue = []
        self.wordfreq = {}
    
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        index = 0
        # print(self.queue, self.stack, self.wordfreq)
        for char in self.queue:
            if self.wordfreq[char] == 1:
                return char
        return "#"
        
    def Insert(self, char):
        # write code here
        if char not in self.wordfreq:
            self.wordfreq[char] = 1
            self.queue.append(char)
        else:
            self.wordfreq[char] += 1
            
        self.stack.append(char)

s = Solution()
s.Insert("g")
print(s.FirstAppearingOnce())
s.Insert("o")
print(s.FirstAppearingOnce())
s.Insert("o")
print(s.FirstAppearingOnce())
s.Insert("g")
print(s.FirstAppearingOnce())
s.Insert("l")
print(s.FirstAppearingOnce())
s.Insert("e")
print(s.FirstAppearingOnce())