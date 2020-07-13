
#
# 
# @param chessboard string字符串一维数组 
# @return string字符串
#
class Solution:
    def playchess(self , chessboard ):
        # write code here
        # 牛妹想要获胜则需要牛牛的将被杀掉，可以先找到牛牛的将再判断能否杀死
        for row_index in range(len(chessboard)):
            chessboard[row_index] = [x for x in chessboard[row_index].strip()]
            if "j" in chessboard[row_index]:
                j_col_index = chessboard[row_index].index("j")
                j_row_index = row_index
        
        chesses = ["j", "p", "b", "c", "J", "P", "B", "C"]
        left_right_chesses = [x for x in chessboard[j_row_index] if x in chesses]
        up_down_chesses = [x[j_col_index] for x in chessboard if x[j_col_index] in chesses]
        # print(left_right_chesses, up_down_chesses)

        def judge(arr):
            for c_index in range(len(arr)):

                if arr[c_index] == "P":
                    if c_index+2 <= len(arr)-1 and arr[c_index+2] == "j":
                        return True
                    if c_index-2 >= 0 and arr[c_index-2] == "j":
                        return True

                if arr[c_index] == "B" or arr[c_index] == "C"  or arr[c_index] == "J":
                    if c_index+1 <= len(arr)-1 and arr[c_index+1] == "j":
                        return True

                    if c_index-1 >= 0 and arr[c_index-1] == "j":
                        return True
            
            return False

        res_left_right = judge(left_right_chesses)
        if res_left_right:
            return "Happy"

        res_up_down = judge(up_down_chesses)
        if res_up_down:
            return "Happy"
        else:
            return "Sad"
            

# print(Solution().playchess(["......", "..B...", "P.C.j.", "......", "..b..."," ...J.." ]))
# print(Solution().playchess(["j....C", "......", "......", "......", "......", ".....J"]))
print(Solution().playchess([".............c...................B..", "..J.........P.......................", "....................................", "....p...............................", "....................................", "....................................", "....................................", "....................................", "....................................", "......................b.....jC......", "....................................", "....................................", "....................................", "...................................."]))