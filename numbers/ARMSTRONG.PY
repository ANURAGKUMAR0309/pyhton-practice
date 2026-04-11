n = int(input("enter number"))

def armstrong(n):
    result =0
    original =n
    digits =len(str(n))
    while(n>0):
        lastdigit = n %10
        result = result + lastdigit **digits
        n = n //10
    return (original == result)
           
print(armstrong(n))