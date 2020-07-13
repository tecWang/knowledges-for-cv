#
# 
# @param n int整型 n
# @param Stick int整型一维数组 Stick
# @return long长整型一维数组
#
#
# 
# @param n int整型 n
# @param Stick int整型一维数组 Stick
# @return long长整型一维数组
#
class Solution:
    def MaxArea(self , n , Stick ):
        # write code here
        # 从收益率的角度来讲
        # 正方形每条边的收益率为 1/4
        # 正三角形每条边的收益率为 sqrt(3)/(4*3)
        # 正方形的收益率会高一些
        # 所以优先构建正方形更合适
        # 还有一个问题就是，可能会存在不同长度的火柴
        
        # 可以先假设所有火柴都是定长的等于1
        def max_area(n, val):
            max_square = n // 4
            rest_stickers = n % 4
            
            if rest_stickers == 0:
                return [0, val**2*max_square]
            else:
                if rest_stickers >= 3:
                    cur_triangle = 1
                else:
                    cur_triangle = 0
                # cut_from_square = 3 - rest_stickers
                # cur_square = max_square - cut_from_square
                # cur_triangle = cut_from_square + 1
                return [val**2*cur_triangle, val**2*max_square]
        
        data_dict ={}
        for i in range(n):
            if Stick[i] not in data_dict.keys():
                data_dict[Stick[i]] = 1
            else:
                data_dict[Stick[i]] += 1
        print(data_dict)

        res = [0, 0]
        for item in data_dict.keys():
            temp_res = max_area(data_dict[item], item)
            print(data_dict[item], item, temp_res)
            res[0] += temp_res[0]
            res[1] += temp_res[1]
        
        return res

s = Solution().MaxArea(13, [1, 1, 1, 1,
                            2, 2, 2, 2,
                            3, 3, 3, 3, 3])
print(s)