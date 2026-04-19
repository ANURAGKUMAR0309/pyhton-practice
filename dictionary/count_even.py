dict = {
    "a":int(input("enter 1st number ")),
    "b": int(input("enetr 2nd number ")),
    "c": int(input("enter 3rd number "))
}
count =0
for value in dict.values():
    if value % 2 ==0:
        count +=1
print("the count of  even numbers :",count)