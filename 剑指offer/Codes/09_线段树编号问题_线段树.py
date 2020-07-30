a = input().split(",[")[-1][:-1].split(",")
ans = []
for i in range(len(a)):
    high = int(a[i])
    res = 1
    while high > 1:
        mid = high//2
        if high % 2 == 1 and not ((mid)&(mid-1)):
            high = mid + 1
            res *= 2
        else:
            high = mid
            res = res*2 + 1
    ans.append(str(res))
print("[" + ",".join(ans) + "]")