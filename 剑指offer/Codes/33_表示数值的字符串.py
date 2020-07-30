# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    
    # 统计规则
    # 1. 首位数字上，不能有".",且只能出现在e之前
    # 2. 首位数字上，可以有"+, -"，且只能在首位上
    # 3. "+","-","."都只能出现一次
    # 4. 不能有无关字母出现在字符串里，除了大写字母e及小写字母e
    def isNumeric(self, s):
        # write code here
        start_e = False
        point_cnt = 0
        
        if s[0] == ".":
            return False
        
        if s[0] == "+" or s[0] == "-":
            s = s[1:]
        
        for ch_index in range(len(s)):
            # print(s[ch_index])
            # 如果是正常的正负号，直接通过
            if s[ch_index] == ".":
                if start_e: 
                    return False
                else:
                    point_cnt += 1
                    # print("point_cnt", point_cnt)
                    if point_cnt > 1:
                        return False
            elif s[ch_index] == "+" or s[ch_index] == "-":
                if s[ch_index-1] != "e" and s[ch_index-1] != "E":
                    return False
            
            # 如果是正常的数字，直接通过
            if ord(s[ch_index]) <= ord("9") and ord(s[ch_index]) >= ord("0"):
                continue
            
            # 处理小数点的位置
            if s[ch_index] == "e" or s[ch_index] == "E":
                # e开始后，小数点和正负号都是不允许的
                start_e = True
                if ch_index == len(s)-1:
                    return False
                
            elif ord(s[ch_index]) >= ord("a") and ord(s[ch_index]) <= ord("z"):
                return False
            elif ord(s[ch_index]) >= ord("A") and ord(s[ch_index]) <= ord("Z"):
                return False
        
        return True

print(Solution().isNumeric("1a3.14"))
print(Solution().isNumeric("1.2.3"))