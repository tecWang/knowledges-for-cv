def Contain1(n):
    print(bin(n), bin(n<<1), bin(n>>1), bin(n & (n<<1)))
    return n & (n<<1) > 0

print(Contain1(1))
print("===============================")
print(Contain1(12))
print("===============================")
print(Contain1(123))
print("===============================")
print(Contain1(1234))
print("===============================")
print(Contain1(-12345))

print("===============================")
print("===============================")
print(bin(12), len(bin(12)))
for i in range(len(bin(12))):
    print(bin(12)[i])

print(oct(12))

print(hex(12))