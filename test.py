a = int(input())
b = [int(x) for x in input().split(" ")]

cnt = 0
for index in range(len(b)-1):
    max_val = max(b[:len(b)-index])
    if max_val == b[len(b)-1-index]:
        continue
    else:
        max_index = b.index(max_val)
        temp_index = max_index
        temp = b[max_index]
        while temp_index < len(b)-1-index:
            b[temp_index] = b[temp_index+1]
            temp_index += 1
        b[temp_index] = max_val
        cnt += 1

print(cnt)

# 4 1 2 5 3