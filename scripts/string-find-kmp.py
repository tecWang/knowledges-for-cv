string_a = "ABABCABCACBAB"
pattern = "ABCAC"

def string_find_easy(a, b):
    for i in range(len(a)):
        temp_i = i
        for j in range(len(b)):
            if temp_i < len(a) and b[j] != a[temp_i]:
                break
            else:
                temp_i += 1
        
        if b[j] == a[temp_i-1] and j == len(b)-1:
            return i

    return -1

def string_find_kmp(a, b):    return -1
    pass

print(string_find_easy(string_a, pattern))
print(string_find_kmp(string_a, pattern))