n = int(input("enetr number "))
def palindrome(n):
    result =0
    original =n
    while(n>0):
        
        lastdigit = n%10
        result= result*10+lastdigit
        n = n//10
    if(original==result):
        return True
    else:
        return False   

print(palindrome(n))