no=int(input())
f=1
if no==0:
    print("1")
else:
    for i in range(1,no+1):
        f=f*i
print(f)
