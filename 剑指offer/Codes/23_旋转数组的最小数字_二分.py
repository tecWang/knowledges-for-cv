# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []:
            return 0
        # 非递减序列并不意味着是一个递增数列
        # 这句话只是想说直接返回数组最后一个元素的行为是不对的
        # 按找本题的意思，大致是分为两端单增数列的
        
        # 必须选择右端点作为target
        # 使用二分法
        low = 0; high = len(rotateArray)-1
        
        while low < high:
            mid = (low+high)//2
            if rotateArray[low] <= rotateArray[high]:
                return rotateArray[low]
            
            if rotateArray[mid] < rotateArray[high]:
                # 答案在左侧
                high = mid
            elif rotateArray[mid] > rotateArray[high]:
                # 答案在右侧
                low = mid + 1
            else:
                high -= 1
                
        return rotateArray[low]

print(Solution().minNumberInRotateArray([5,6,1,2,3,4]))
print(Solution().minNumberInRotateArray([5,6,7,8,1,2,3,4]))
print(Solution().minNumberInRotateArray([1,2,3,4,5,6,7,8]))