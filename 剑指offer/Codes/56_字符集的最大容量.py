n = int(input())
data = []
for i in range(n):
    data.append("".join(sorted([x for x in input()])))

res = {}
for val in data:
    if val not in res.keys():
        res[val] = 1
    else:
        res[val] += 1

# res.sort()
print(sorted(res.items(), key=lambda x:x[1])[-1][1])

'''
8
abc
abcd
acb
bca
bac
bcda
cba
cab
'''