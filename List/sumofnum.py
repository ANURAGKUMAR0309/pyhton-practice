n = int(input("enetr how many number:"))
x = []
total =0
for i in range(n):
    num = int(input("enter number"))
    x.append(num)
    total = total+num
print(x)
print("total sum is ", total)    