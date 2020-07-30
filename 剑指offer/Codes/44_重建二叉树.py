# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from libs.tree import inorder, TreeNode

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here

        def build_tree(pre, tin):
            if pre == [] or tin == []:
                return

            # print(pre, tin, end=", ")
            root_val = pre.pop(0)
            index = tin.index(root_val)
            tin_left = tin[:index]
            tin_right = tin[index+1:]
            # print(root_val, tin_left, tin_right)

            root = TreeNode(root_val)
            if tin_left != []:
                root.left = build_tree(pre[:len(tin_left)], tin_left)
            if tin_right != []:
                root.right = build_tree(pre[len(tin_left):], tin_right)

            return root
    
        if pre == [] or tin == []:
            return None

        return build_tree(pre, tin)

root = Solution().reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
print(inorder(root))
print("=========================")
root = Solution().reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7])
print(inorder(root))