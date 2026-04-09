n= int(input("enter number"))
def reverse(n):
    result =0 
    while(n>0):
        lastdigit = n%10
        result = result*10+lastdigit
        n = n//10
    return result
print(reverse(n))    