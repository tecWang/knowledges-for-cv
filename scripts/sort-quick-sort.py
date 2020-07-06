arr = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]

def quick_sort(left, right):

    if left > right:
        return

    print("arr", arr)
    temp = arr[left]    # 左侧第一个元素作为基准数
    i = left
    j = right

    while i != j:

        while arr[j] >= temp and i < j:
            j -= 1
        
        while arr[i] <= temp and i < j:
            i += 1

        if i < j:
            c = arr[i]
            arr[i] = arr[j]
            arr[j] = c

    arr[left] = arr[i]
    arr[i] = temp

    quick_sort(left, i-1)
    quick_sort(i+1, right)

    return

quick_sort(0, len(arr)-1)