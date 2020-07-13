# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 从左下进行查找
        n_row = len(array)
        n_col = len(array[0])

        if n_row == 0:
            return False

        if n_col == 0:
            return False

        # 二维空间的二分法跟想象中还是有很大不同的
        # 不应该机械的先锁定列再找行
        # 而是动态的选择在数组中移动
        row = n_row - 1
        col = 0
        while row >=0 and col <= n_col-1:
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                col += 1
            else:
                row -= 1

print([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
print(Solution().Find(7, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
# print(Solution().Find(1, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
# print(Solution().Find(16, [[]]))


