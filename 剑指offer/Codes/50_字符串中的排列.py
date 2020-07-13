# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        chars = [val for val in ss]

        res = []
        def dfs(arr, str):
            if arr == []:
                return str
            
            for index, val in enumerate(arr):
                new_str = dfs(arr[:index] + arr[index+1:], str+val)
                if new_str:
                    res.append(new_str)
            
        
        dfs(chars, "")
        return sorted([i for i in set(res)])

print(Solution().Permutation("abc"))
print(Solution().Permutation("aa"))