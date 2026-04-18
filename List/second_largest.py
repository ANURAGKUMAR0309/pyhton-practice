num = list(map(int,input("enetr number ").split()))
Largest = float('-inf')
Second_largest = float('-inf')
for el in num:
    if(el >Largest):
        Second_largest=Largest
        Largest = el
    elif(el > Second_largest and el != Largest):
        Second_largest = el
if(Second_largest== float('-inf')):
    print("none second largest element found ")
else:
    print("This is the second largest number:", Second_largest)        