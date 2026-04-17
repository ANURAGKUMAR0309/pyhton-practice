num =int(input("enetr number "))
original = num
result = 0
while(num>0):
    last_digit = num%10
    fact = 1
    for i in range(1,last_digit+1):
        fact = fact * i
    result = result + fact 
    num = num // 10
if(original == result):
    print("this is strong number ")
else:
    print("this is not strong number")         
print(result)
