a = input().split()
s = [int(x) for x in a if int(x) > 0]
print(len(a) - len(s))
print("{:.1f}".format(sum(s)/len(s)))

# input
# 18259 3386 -3490 64453 -1571 57543 12151 2186 -17851 56212 42919 48020 -409 13979 49103 -4985 28018 -13005 21866 48272 17400 76308 49960 22177 -19074 40860 35215 -1608 69665 70068 1127 16417 42894 36660 66927 24406 -8651 34582 57412 -5440 -2059 26052 11727 68881 30676 19227 -13007 67727 13582 72918 66762 -15575 25595 -8260 68470 75520 10708