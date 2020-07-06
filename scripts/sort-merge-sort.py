arr = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]

def merge_sort(arr):

    # print("arr",arr, "len(arr)", len(arr))
    if len(arr) < 2:    # 即归并到只剩一个元素了
        return arr

    mid = (0 + len(arr) - 1) >> 1
    left = merge_sort(arr[0:mid+1])
    # print("left finished")
    right = merge_sort(arr[mid+1:])
    # print("right finished")

    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if left:
        result += left

    if right:
        result += right

    print("result", result)
    return result

merge_sort(arr)