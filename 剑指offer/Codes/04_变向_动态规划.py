# class Solution:
#     def solve(self , n , a1 , a2 , a3 , m ):
#         if n == 0:
#             return 0
        
#         for i in range(1, n):
#             # 这种决策方式，比较短视昂
#             pre_m = m[i-1]
#             pre_a1 = a1[i-1]; pre_a2 = a2[i-1]; pre_a3 = a3[i-1];
#             a1[i] += max(pre_a1, pre_a2-pre_m)
#             a3[i] += max(pre_a3, pre_a2-pre_m)
#             a2[i] += max(pre_a2, pre_a1-pre_m, pre_a3-pre_m)
        
#         return max(a1[n-1], a2[n-1], a3[n-1])


# print(Solution().solve(3,[1,9,3],[6,4,6],[1,1,5],[3,2,1]))

# test1   3,[1,9,3],[6,4,6],[1,1,5],[3,2,1]
# test2   2,[7072,2415],[4217,1170],[3218,216],[7431,362]

n , a1 , a2 , a3 , m = input().split(",[")
n = int(n)
a1 = [int(x) for x in a1[:-1].split(",")]
a2 = [int(x) for x in a2[:-1].split(",")]
a3 = [int(x) for x in a3[:-1].split(",")]
m = [int(x) for x in m[:-1].split(",")]

if n == 0:
    print(0)

for i in range(1, n):
    # 这种决策方式，比较短视昂
    pre_m = m[(i-1)]
    pre_a1 = a1[(i-1)]; pre_a2 = a2[(i-1)]; pre_a3 = a3[(i-1)];
    # print(pre_a1, pre_a2, pre_a3)
    a1[i] += max(pre_a1, pre_a2-pre_m)
    a3[i] += max(pre_a3, pre_a2-pre_m)
    a2[i] += max(pre_a2, pre_a1-pre_m, pre_a3-pre_m)

print(max(a1[(n-1)], a2[(n-1)], a3[(n-1)]))