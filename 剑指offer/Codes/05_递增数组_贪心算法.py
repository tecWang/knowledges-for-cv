#
# 
# @param array int整型一维数组 array
# @return long长整型

# 错误解法
# 因为这么算没有考虑区间的概念，导致很多元素被反复算了很多遍
class Solution:
    def IncreasingArray(self , array ):
        # write code here
        # 遍历数组，保证下一个元素至少比上一个元素大一
        pre = array[0]
        total = 0
        for i in range(1, len(array)):
            cur = array[i]
            # print("pre", pre, "cur", cur)
            if cur <= pre:
                diff = pre - cur + 1
                # print("diff", diff)
                total += diff
                pre = cur + diff
            else:
                pre = cur

        return total

class Solution2:
    def IncreasingArray(self , array ):
        total = 0
        for i in range(1, len(array)):
            if array[i] <= array[i-1]:
                total += array[i-1] - array[i] + 1

        return total

# print(Solution().IncreasingArray([1,2,1]))
print(Solution().IncreasingArray([1, 2, 3, 4, 5, 5, 5, 7, 6]))
print(Solution2().IncreasingArray([1, 2, 3, 4, 5, 5, 5, 7, 6]))