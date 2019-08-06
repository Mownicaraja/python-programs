num=int(input())
t=0
while(num>0):
    d=num%10
    t=t+d
    num=num//10
rev=0
s=t
while(s>0):
    rem=s%10
    rev=(rev*10)+rem
    s=s//10
if(t==rev):
    print("YES")
else:
    print("NO")

