a = input()
arr = input()
arr = [int(x) for x in arr]

# 8 
# 10000011

a = 0; b = 0;
index = 0
for index in range(len(arr)):

    if index == len(arr)-1:
        continue

    if arr[index] == arr[index+1]:
        a += 1
    else:
        b += 1

print(b + 1 + min(2, a))