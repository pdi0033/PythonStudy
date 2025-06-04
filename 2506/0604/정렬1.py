def selectSort1(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    return arr

arr = [9, 7, 25, 6, 8, 4, 3]
print(selectSort1(arr))

def selectSort2(arr):
    for i in range(0, len(arr)-1):
        min = arr[i]
        pos = i
        for j in range(i+1, len(arr)):
            if min > arr[j]:
                min = arr[j]
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]
        print(arr)
    return arr

print()
arr = [9, 7, 25, 6, 8, 4, 3]
print(selectSort2(arr))