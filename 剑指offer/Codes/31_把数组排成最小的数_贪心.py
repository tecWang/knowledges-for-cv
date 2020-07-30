# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        arr = [num for num in numbers]
        arr.sort()
        print(arr)
        return "".join([str(a) for a in arr])

print(Solution().PrintMinNumber([1, 12, 123]))
print(Solution().PrintMinNumber([3, 32, 321]))