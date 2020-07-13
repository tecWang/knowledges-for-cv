import functools

def func(x,y):
    print(type(x+y), type(y+x))
    if x+y < y+x:
        return -1
    else:
        return 1
    return 0

# a = [1, 12, 123]
# a = [3, 32, 321]
a = [str(val) for val in a]
a.sort(key=functools.cmp_to_key(func))
print(a)