class Solution:
    def solve(self , n , m , x , y ):
        # write code here
        # 3 rows, n cols
        dp = [[0 for i in range(n)] for j in range(3)]
        # 标记路障为-1, m stops
        for stop_index in range(m):
            print(stop_index, x[stop_index], y[stop_index])
            dp[x[stop_index]-1][y[stop_index]-1] = -1

        print(dp)
        dp[0][0] = 1
        dp[1][0] = 0
        dp[2][0] = 0
        # 按列更新数据看起来容易很多
        for c_index in range(1, n):
            # 因为牛牛一定从一列出发，因为第一列可以被跳过
            for r_index in range(3):
                
                if dp[r_index][c_index] == -1:
                    continue                    

                # 第二行的时候，有三种方式可以达到某个点
                if r_index == 0:

                    dp[r_index][c_index] += dp[r_index][c_index-1] + \
                                            dp[r_index+1][c_index-1]
                    if dp[r_index][c_index-1] == -1:
                        dp[r_index][c_index] += 1
                    if dp[r_index+1][c_index-1] == -1:
                        dp[r_index][c_index] += 1

                elif r_index == 1:    # 不需要担心行索引越界，因为行数确定
                    dp[r_index][c_index] += dp[r_index-1][c_index-1] + \
                                            dp[r_index][c_index-1] + \
                                            dp[r_index+1][c_index-1]
                    if dp[r_index-1][c_index-1] == -1:
                        dp[r_index][c_index] += 1
                    if dp[r_index][c_index-1] == -1:
                        dp[r_index][c_index] += 1
                    if dp[r_index+1][c_index-1] == -1:
                        dp[r_index][c_index] += 1

                elif r_index == 2:
                    dp[r_index][c_index] += dp[r_index-1][c_index-1] + \
                                            dp[r_index][c_index-1]
                    if dp[r_index-1][c_index-1] == -1:
                        dp[r_index][c_index] += 1
                    if dp[r_index][c_index-1] == -1:
                        dp[r_index][c_index] += 1
                
                dp[r_index][c_index] = dp[r_index][c_index] % (1000000007)

        return dp[r_index][c_index]


print(Solution().solve(4,1,[1],[2]))
