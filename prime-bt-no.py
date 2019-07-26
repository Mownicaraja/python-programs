m,n=map(int,input().split())
for p in range(m+1,n):
    if p>1:
        for i in range(2,p):
            if(p%i)==0:
                break
        else:
            print(p,"",end="")
