# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        low = 0; high = len(data)-1
        while low < high:
            mid = (low+high)>>1
            print("low, mid, high", low, mid, high, "|||", data[low], data[mid], data[high])
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid
            else:
                high -= 1

        cnt = 0
        while low <= len(data)-1 and data[low] == k:
            cnt += 1
            low += 1
        return cnt

            

        # return data.count(k)

data = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]
print(data.index(2))
print(Solution().GetNumberOfK(data, 2))
data = [1,2,3,3,3,3]
print(data.index(3))
print(Solution().GetNumberOfK(data, 3))