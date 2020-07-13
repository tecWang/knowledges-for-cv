# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        # suppose this tree is BST, if success then return True, else return False
        def judge(arr):
            # print(arr)
            if arr == []:
                return
            
            root = arr[-1]    # get root node
            left = []
            index = 0
            while arr[index] < root:
                left.append(arr[index])
                index += 1
            right = arr[index:-1]
            for val in right:
                if val < root:
                    return False

            judge(left)
            judge(right)
        
            return True

        if sequence == []:
            return False

        return judge(sequence)

print(Solution().VerifySquenceOfBST([0, 1, 3, 2, 5, 7, 6, 4]))
# print(Solution().VerifySquenceOfBST([8, 4, 5, 2, 6, 7, 3, 1]))
