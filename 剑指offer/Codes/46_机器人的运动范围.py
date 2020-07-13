# -*- coding:utf-8 -*-
class Solution:
    
    def __init__(self):
        self._dict = {}
        self.cnt = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        
        def sum_of_num(num):
            if num == 0:
                return 0
            
            arr = []
            while num > 0:
                arr.append(num % 10)
                num = num // 10
            return sum(arr)

        # 三个终止条件: 越界，重复，超过阈值
        def dfs(x, k, i, j):
            # 越界
            if not (0 <= i <= rows-1 and 0 <= j <= cols-1):
                return
            # 重复
            if self._dict.get((i, j)) is not None:
                return
            # 超过阈值
            if sum_of_num(i) + sum_of_num(j) > k:
                return
            
            self.cnt += 1
            self._dict[(i,j)] = 1
            dfs(x, k, i+1, j)
            dfs(x, k, i-1, j)
            dfs(x, k, i, j+1)
            dfs(x, k, i, j-1)

        # 沿着横向走，把所有横向的情况都列举出来
        x = [[1 for col in range(cols)] for row in range(rows)]
        dfs(x, threshold, 0, 0)

        return self.cnt

print(Solution().movingCount(15, 20, 20))
print(Solution().movingCount(10, 1, 100))
