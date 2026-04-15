arr = list(map(int, input("enter elements: ").split()))
target = int(input("enter target: "))

def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

print(two_sum(arr, target))      