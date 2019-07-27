m,n=map(int,input().split())
t=n
s=0
l=[]
l=list(map(int,input().strip().split()))[:m]
for i in range(0,t):
  s=s + l[i]
print(s)
