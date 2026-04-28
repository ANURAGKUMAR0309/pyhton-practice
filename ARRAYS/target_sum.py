arr = list(map(int, input("Enter array elements ").split()))
x = int(input("Enter target number: "))

def targetsum(arr, x):
   
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == x:
            return True
        elif current_sum < x:
            left += 1
        else:
            right -= 1
            
    return False        

print(targetsum(arr, x))