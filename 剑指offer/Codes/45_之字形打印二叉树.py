from libs.tree import build_tree_from_array, preorder

root = build_tree_from_array(None, [1, 
                                    2, 3, 
                                    4, "#", 5, 6, 
                                    "#", 7, "#", "#", "#", "#", 8, "#"], 0)
# root = build_tree_from_array(None, [8,"#",8,"#",9,"#",2,"#",5])
print(root.val)
print(preorder(root))

class Solution:
    def Print(self, pRoot):

        if pRoot == None:
            return []

        # write code here
        cur_level = [pRoot]
        next_level = []
        is_odd = True
        res = []
        layer_res = []
        while cur_level:

            node = cur_level.pop(0)
            layer_res.append(node.val)
            # print(is_odd, res, node.val, node.left, node.right)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            if len(cur_level) == 0:
                # print("change odd, ============================")
                if not is_odd:
                    layer_res.reverse()
                res.append(layer_res)
                cur_level = next_level
                next_level = []
                layer_res = []

                is_odd = not is_odd

        return res

    def Print2(self, pRoot):
        # write code here
        # 不能用栈实现，应该用队列保证先进先出的顺序才可以
        queue = [pRoot]
        res = []
        odd = True
        while len(queue) != 0:
            size = len(queue)    # 确定好当前行需要出栈几个节点
            row = []
            for i in range(size):
                node = queue.pop(0)
                if node != None:
                    row.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if row:
                if odd:
                    res.append(row)
                else:
                    row.reverse()
                    res.append(row)
            odd = not odd
        return res

# print(Solution().Print(root))
print(Solution().Print2(root))