List = list(map(int,input().split()))
max_elem = 0
for i in List:
    if i > max_elem:
        max_elem = i
print(max_elem)