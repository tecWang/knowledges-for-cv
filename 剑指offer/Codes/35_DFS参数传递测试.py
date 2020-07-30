# -*- coding:utf-8 -*-
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        # DFS
        def dfs(root, target, path, res):

            if root == None:
                return
    
            if root != None:
                path.append(root.val)
                # print("root.val, target, path", root.val, target, path)
            
            if root.val == target and root.left == None and root.right == None:
                # print("path", path)
                res.append(copy.deepcopy(path))
            
            dfs(root.left, target-root.val, copy.deepcopy(path), res)
            dfs(root.right, target-root.val, copy.deepcopy(path), res)

            return res
        
        if root == None:
            return []
            
        res = dfs(root, expectNumber, [], [])
        return res

# {10,5,12,4,7},22
node = TreeNode(10)
node.left = TreeNode(5)
node.right = TreeNode(12)
node.left.left = TreeNode(4)
node.left.right = TreeNode(7)

res = Solution().FindPath(node, 22)
res = Solution().FindPath(node, 15)
print(res)
        
