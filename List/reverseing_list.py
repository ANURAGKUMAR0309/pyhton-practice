arr = list(map(int,input("enetr elements ").split()))
left = 0
right = len(arr)-1
while(left<right):
    arr[left] ,arr[right] = arr[right],arr[left]
    left +=1
    right -=1
print("this is reversed list ",arr)    