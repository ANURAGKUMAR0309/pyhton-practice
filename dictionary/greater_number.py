data = {
    "num1": int(input("enter 1st number ")),
    "num2": int(input("enter 2nd number ")),
    "num3": int(input("enter 3rd number "))
}
x = int(input("enter target value "))
for key,value in data.items():
    if value>x:
        print(key,value)