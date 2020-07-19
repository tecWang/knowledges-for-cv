n = int(input())
data = []
for i in range(n):
    data.append(input())

MAX_LEN = 8
def AddString(string):
    rest_zero = MAX_LEN - len(string)
    return string + "".join([str(0) for i in range(rest_zero)])

for temp_str in data:
    str_len = len(temp_str)
    if str_len < MAX_LEN:
        print(AddString(temp_str))
    else:
        # 拆分输出或直接输出
        while len(temp_str) > 8:
            print(temp_str[:8])
            temp_str = temp_str[8:]
        print(AddString(temp_str))

'''
# input
5
wx
x54on1s73ubb9c
f29iiqb28l72k
y
y5vor
'''