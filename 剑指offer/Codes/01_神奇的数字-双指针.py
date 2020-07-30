#
# 
# @param number string字符串 
# @return string字符串
#
class Solution:
    def change(self , number ):
        # write code here
        start = 0
        end = len(number) - 1
        number = list(number)
        while start < end:
            # 偶数位，对调
            print(start, end)
            if int(number[start]) % 2 == 0:
                # 此时可以去寻找末尾开始的第一个偶数
                while int(number[end]) % 2 != 0:
                    end -= 1
                
                # 两数交换
                temp = number[start]
                number[start] = number[end]
                number[end] = temp
                end -= 1
                
            start += 1
            
        return "".join(number)