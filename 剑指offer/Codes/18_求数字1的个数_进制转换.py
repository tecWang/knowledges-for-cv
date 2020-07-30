
def NumberOf1(num):
    return bin(num).count("1")

print(NumberOf1(12))
print("==========================")
print(NumberOf1(-12))


def NumberOf1_version2(num):
    count = 0
    while num != 0:
        count += 1
        ''' 
            print("bin(num)", bin(num))
            bin(num) -0b1100
            bin(num) -0b10000
            bin(num) -0b100000
            bin(num) -0b1000000
            bin(num) -0b10000000
            bin(num) -0b100000000
            bin(num) -0b1000000000
            bin(num) -0b10000000000
            bin(num) -0b100000000000
            bin(num) -0b1000000000000
        '''
        num = num & (num-1)
        if count >= 10:
            return -1
    return count

print(NumberOf1_version2(12))
print("==========================")
print(NumberOf1_version2(-12))  # infinite loop


