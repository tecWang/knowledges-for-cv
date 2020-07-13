#
# 
# @param n int整型 n个人
# @param a int整型一维数组 ai代表第i个人的高度
# @return long长整型
#
class Solution:
    def solve(self , n , a ):
        # write code here
        index = n - 1
        SUM = 0
        while index > 0:
            temp_index = index - 1
            while a[temp_index] < a[index]:
                # 如果已经到了第一个位置，还没有找到比自己高的元素，则自己是最高的
                if temp_index == 0:
                    SUM += 0
                    break    
                temp_index -= 1
                
            SUM += temp_index + 1 
            print("SUM", SUM, temp_index + 1)

            index -= 1
 
        return SUM
            
# print(Solution().solve(5,[1,2,3,4,5]))
# print(Solution().solve(5,[5,4,3,2,1]))