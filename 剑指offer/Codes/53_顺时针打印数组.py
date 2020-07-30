# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        
        res = []
        x = 0; y = 0; direction = 0;
        while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and vis[x][y] == 0:
            dx, dy = directions[direction]
            # print(x, y, dx, dy, matrix[x][y])
            res.append(matrix[x][y])
            vis[x][y] = 1
            
            # 沿着当前方向继续走
            while 0 <= x+dx < len(matrix) and 0 <= y+dy < len(matrix[0]) and vis[x+dx][y+dy] == 0:
                x += dx; y += dy;
                res.append(matrix[x][y])
                vis[x][y] = 1
            
            direction = (direction + 1) % 4
            dx, dy = directions[direction]
            x += dx; y += dy;
        
        return res

print(Solution().printMatrix([[1,2],[3,4]]))