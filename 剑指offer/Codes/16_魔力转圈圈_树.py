pre, l, r, k = input().split(",[")
l = [int(x) for x in l[:-1].split(",")]
r = [int(x) for x in r[:-1].split(",")]
k = [int(x) for x in k[:-1].split(",")]

def InOrder(root, l, r):

    stack = []
    res = "["
    while stack != [] or root != 0:
        # stack.append(root)
        while root != 0:
            stack.append(root)
            root = l[root-1]    # 左子树成为新的根节点
        # print("stack", stack)

        root = stack.pop()
        res += str(root) + ","
        if r[root-1] != 0:      # 如果这个节点还有右节点，加入栈内
            root = r[root-1]
        else:
            root = 0

    return res[:-1] + "]"

def solve(n , m , l , r , k ):
    # write code here
    data = [0 for i in range(len(l))]
    for key in k:
        # 否则找到左右子树没有子节点为止
        kks = []
        kks.append(key)
        while kks != []:
            sub_node = kks.pop() - 1
            
            if l[sub_node] != 0:
                kks.append(l[sub_node])
            if r[sub_node] != 0:
                kks.append(r[sub_node])

            if l[sub_node] != 0 or r[sub_node] != 0:
                data[sub_node] += 1 
    
    for i in range(len(data)):
        if data[i] % 2 != 0:
            temp = l[i]
            l[i] = r[i]
            r[i] = temp

    print(data)
    print("l, r", l, r)
    return InOrder(1, l, r)

# test 5,3,[4,3,0,0,0],[2,0,0,5,0],[3,1,5]
# test2 11,3,[2,4,6,8,0,10,0,0,0,0,0],[3,5,7,9,0,0,11,0,0,0,0],[6,3,2]
print(solve(0, 0, l, r, k))
