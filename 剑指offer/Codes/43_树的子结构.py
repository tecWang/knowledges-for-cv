# -*- coding:utf-8 -*-
from libs.tree import build_tree, preorder

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None:
            return False
        
        # 遍历两棵二叉树
        def pre_order(root):
            string = ""
            if root == None:
                return string
            
            stack = []
            while root:
                string += str(root.val)
                stack.append(root)
                root = root.left
            
            while stack:
                node = stack.pop()
                if node.right:
                    string += str(node.right.val)
                    temp = node.right
                    stack.append(temp)
                    while temp.left:
                        string += str(temp.left.val)
                        stack.append(temp.left)
                        temp = temp.left
                        
            return string
        
        str1 = pre_order(pRoot1)
        str2 = pre_order(pRoot2)
        # print(str1, str2)
        if str2 in str1:
            return True
        else:
            return False

root1 = build_tree(None, [8,"#",8,"#",9,"#",2,"#",5])
print(preorder(root1))
root2 = build_tree(None, [8,"#",9,"#",2])
print(preorder(root2))

print(Solution().HasSubtree(root1, root2))
