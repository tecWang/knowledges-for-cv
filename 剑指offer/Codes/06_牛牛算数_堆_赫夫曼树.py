pre, a = input().split(",[")
n, c = pre.split(",")
n = int(n)
c = int(c)
a = [int(x) for x in a[:-1].split(",")]

def build_heffman_tree(a):
    total = 0
    while(len(a) != 1):
        # a.sort(reverse=True)
        a.sort()
        # 最小的是左节点，大一点的是右节点
        lc = a.pop(0)
        rc = a.pop(0)
        total += lc + rc
        a.append(lc + rc)
            
    return a[0], total # 返回赫夫曼树根节点
            

# test1   5,76,[81,30,76,24,84]
_, total = build_heffman_tree(a)
print(total*c)
# print(total*c, a[0]*c)
    
