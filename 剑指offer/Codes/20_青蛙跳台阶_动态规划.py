class Solution:
    def jumpFloor(self, number):
        # write code here
        dp = [0 for i in range(number)]
        dp[0] = 1
        dp[1] = 2
        for j in range(2, number):
            dp[j] = dp[j-1] + dp[j-2]
        return dp[number-1]

print(Solution().jumpFloor(10))