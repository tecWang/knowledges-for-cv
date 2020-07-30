
pre, x = input().split(",[")
n, m = pre.split(",")
n = int(n)
m = int(m)
x = [int(i) for i in x[:-1].split(",")]


sum_x = 0
max_x = 0
for i in range(len(x)):
    sum_x += x[i]
    if x[i] > max_x:
        max_x = x[i]

rest = n - (sum_x - max_x)
c = 0
while rest > max_x:
    c += 1
    max_x *= 2

print(c)        
