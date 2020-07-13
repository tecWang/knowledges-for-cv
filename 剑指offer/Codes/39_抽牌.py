# -*- coding:utf-8 -*-
class Solution:

    def IsContinuous(self, numbers):
        # write code here
        if numbers == []:
            return False

        numbers.sort()
        while numbers[0] == 0:
            numbers.pop(0)
            
        for val in numbers:
            if numbers.count(val) > 1:
                return False

        if (max(numbers) - min(numbers)) >= 5:
            return False
        
        return True

print(Solution().IsContinuous([1,3,2,6,4]))
print(Solution().IsContinuous([0,3,2,6,4]))