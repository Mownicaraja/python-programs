no=int(input())
f=1
if(no<=20 and no==0):
    print("1")
elif(no<20):
    for i in range(1,no+1):
        f=f*i
    print(f)
