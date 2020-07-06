#### 字符串匹配算法

对一个串中某字串得定位操作称为串得模式匹配，其中待定位得子串称为**模式串**，执行定位操作得串称为**主串**。

##### 简单模式匹配算法

算法基本思想:
从主串得第一个位置起和模式串得第一个字符开始比较，
- 如果相等，则继续逐一比较后续字符串
- 否则从主串的第二个字符开始，重新用上一步的方法与模式串中的字符做比较

以此类推，直到比较完模式串中的所有字符。若匹配成功，返回模式串在主串中的位置，若匹配不成功，返回一个可以区别于主串所有位置的标记，如“-1”。

```python
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
print(string_find_easy(string_a, pattern))
```

##### KMP算法匹配算法

