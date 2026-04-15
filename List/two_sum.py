arr = [7,8,5,6,3]
target = 9
def calc_sum(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==target):
                return i,j
print(calc_sum(arr))           