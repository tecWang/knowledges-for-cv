# -*- coding:utf-8 -*-
import copy
class Solution:
    
    # 终止条件：越界，路径不通，字母不符合        
    def dfs(self, matrix, temp_path, i, j):
        if not temp_path:
            return True

        if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])):
            return False

        if temp_path:
            char = temp_path[0]
            if matrix[i][j] != char:
                return False
        
        matrix[i][j] = '0'
        flag1 = self.dfs(matrix, temp_path[1:], i+1, j)
        flag2 = self.dfs(matrix, temp_path[1:], i-1, j)
        flag3 = self.dfs(matrix, temp_path[1:], i, j+1)
        flag4 = self.dfs(matrix, temp_path[1:], i, j-1)
        return flag1 or flag2 or flag3 or flag4

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        matrix_c = []
        for row in range(rows):
            arr_row = []
            for col in range(cols):
                arr_row.append(matrix[row*cols+col])
            matrix_c.append(arr_row)

        temp_path = [val for val in path]
        for i in range(rows):
            for index, val in enumerate(matrix_c[i]):
                if val == temp_path[0]:
                    if self.dfs(copy.deepcopy(matrix_c), copy.deepcopy(temp_path), i, index):
                        return True
        return False

# print(Solution().hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))
# print(Solution().hasPath("ABCESFCSADEE", 3, 4, "SEE"))
print(Solution().hasPath("ABCESFCSADEE",3,4,"ABCB"))
print(Solution().hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SLHECCEIDEJFGGFIE"))