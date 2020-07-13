# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        # 只有奇数和偶数
        for a_i in range(len(array)):
            # 如果是奇数的话，开始调换其身前的所有偶数
            if array[a_i] % 2 != 0:

                if a_i == 0:
                    continue

                # 奇数
                temp = array[a_i]
                k = a_i - 1
                while array[k] % 2 == 0:
                    array[k+1] = array[k]   # 左值给右值
                    k -= 1
                array[k+1] = temp
                
        return array

print(Solution().reOrderArray([1,2,3,4,5,6,7]))