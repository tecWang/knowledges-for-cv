#
# 
# @param presentVolumn int整型二维数组 N*M的矩阵，每个元素是这个地板砖上的礼物体积
# @return int整型
#
class Solution:
    def selectPresent(self , presentVolumn ):
        # write code here
        if presentVolumn == []:
            return 0

        n = len(presentVolumn)
        m = len(presentVolumn[0])

        dp = [[0 for i in range(m)] for j in range(n)]
        dp[0][0] = presentVolumn[0][0]
                
        for r_index in range(n):
            for c_index in range(m):
                if r_index == 0 and c_index == 0:
                    continue
                elif r_index == 0:
                    dp[r_index][c_index] += presentVolumn[r_index][c_index] + dp[r_index][c_index-1] 
                elif c_index == 0:
                    dp[r_index][c_index] += presentVolumn[r_index][c_index] + dp[r_index-1][c_index]
                else:
                    # 正常情况
                    dp[r_index][c_index] += presentVolumn[r_index][c_index] + \
                        min(dp[r_index][c_index-1], dp[r_index-1][c_index], dp[r_index-1][c_index-1])
        return dp[r_index][c_index]

print(Solution().selectPresent([[1,2,3],[2,3,4]]))