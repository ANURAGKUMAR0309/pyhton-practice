num = [4,7,8,2,9]
x = []
def evenonly(num):
    for i in num:
        if(i%2==0):
            x.append(i)
    return x        

print(evenonly(num))