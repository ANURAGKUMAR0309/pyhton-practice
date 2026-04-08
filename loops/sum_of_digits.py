n = int(input("enter number"))
count =0
while(n>0):
    lastdigit= n%10
    count +=1
    n = n//10
print(count)        