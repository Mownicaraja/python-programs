N=int(input())
f=1
if(N<=20 and N==0):
    print("1")
elif(N<=20):
    for i in range(1,N+1):
        f=f*i
    print(f)
