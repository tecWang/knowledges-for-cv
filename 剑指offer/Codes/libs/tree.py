#######################################################################
### 二叉树的创建及遍历
### tecwang@126.com
### 2020.06.27
#######################################################################

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 根据输入的数组顺序建立二叉树
def build_tree_from_array(root, arr, index):
    if index > len(arr)-1:
        return

    # print("index", index, arr[index], end=", ")    
    a = arr[index]

    if a == "#":
        root = None
        # print()
        # return
    else:
        root = TreeNode(a)
        # print(2*index+1, 2*index+2)
        root.left = build_tree_from_array(root.left, arr, 2*index+1)
        root.right = build_tree_from_array(root.right, arr, 2*index+2)

    return root

# 根据前序遍历和中序遍历建立二叉树
def build_tree_from_preorder_and_inorder_array(pre, tin):

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

# 前序遍历
def preorder(root):
    if root == None:
        print("binary tree is none")

    stack = []
    res = []
    # 顺着左子树向下打印
    while root:
        res.append(root.val)
        stack.append(root)
        root = root.left
    
    while stack:
        # print(stack, end=",")
        node = stack.pop()
        # print(node.val)
        # 检查当前节点的右孩子是否存在，存在则打印并入栈
        if node.right:
            # print("res", res)
            res.append(node.right.val)
            stack.append(node.right)
            temp = node.right
            while temp.left:
                res.append(temp.left.val)
                stack.append(temp.left)
                temp = temp.left

    return res

# 中序遍历
def inorder(root):
    pass

# 后序遍历
def postorder(root):
    pass


if __name__ == "__main__":
    root = build_tree_from_array(None, [1, 
                                        2, 3, 
                                        4, "#", 5, 6, 
                                        "#", 7, "#", "#", "#", "#", 8, "#"], 0)
    print(preorder(root))

    root1 = build_tree_from_array(None, [8,
                                        "#",8,
                                        "#","#","#",9,
                                        "#","#","#","#","#","#","#",2,
                                        "#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",5], 0)
    print(preorder(root1))

