arr = list(map(int,input("enter array elements ").split()))

def remove_duplicate(arr):
    if not arr:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

length = remove_duplicate(arr)
print(arr[:length] )
