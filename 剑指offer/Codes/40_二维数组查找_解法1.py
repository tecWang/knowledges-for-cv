# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 二分法吧
        # 先锁定数据在哪一行,比较每列的第一个元素
        # print(len(array[0]))
        if len(array[0]) == 0:
            return False

        for row_index in range(len(array)):
            if array[row_index][0] > target:
                continue
            else:
                arr = array[row_index]
                # print("arr", arr)
                low = 0
                high = len(arr)-1
                while low <= high:
                    mid = (low + high) >> 1
                    # print(low, high, mid, arr[mid])
                    if arr[mid] < target:
                        low = mid + 1
                    elif arr[mid] > target:
                        high = mid - 1
                    else:
                        return True
                
        return False
        
# print(Solution().Find(7, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
# print(Solution().Find(1, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
print(Solution().Find(16, [[]]))


