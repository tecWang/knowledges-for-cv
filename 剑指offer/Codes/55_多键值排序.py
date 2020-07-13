n = input()
robustness = [int(val) for val in input().split()]
correctness = [int(val) for val in input().split()]

robustness_index = sorted(range(len(robustness)), key=lambda k:robustness[k], reverse=True)

val_index = 0
while val_index < len(robustness_index):

    if val_index + 1 == len(robustness_index):
        print(robustness[robustness_index[val_index]], correctness[robustness_index[val_index]])
        break

    if robustness[robustness_index[val_index]] != robustness[robustness_index[val_index+1]]:
        print(robustness[robustness_index[val_index]], correctness[robustness_index[val_index]])
        val_index += 1
    else:
        temp_index = val_index
        stack = []
        temp_val = robustness[robustness_index[temp_index]]
        while temp_val == robustness[robustness_index[temp_index+1]]:
            stack.append(correctness[robustness_index[temp_index]])
            temp_index += 1
        stack.append(correctness[robustness_index[temp_index]])
        stack = sorted(stack, reverse=True)
        for val in stack:
            print(temp_val, val)
        val_index = temp_index + 1
