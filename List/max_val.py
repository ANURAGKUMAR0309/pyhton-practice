arr = list(map(int, input("enter elements: ").split()))

max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print("Maximum element is:", max_val)  