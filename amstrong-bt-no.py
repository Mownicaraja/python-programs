q,n=map(int,input().split())  
for i in range(q,n):
   s=0
   t=i
   while t>0:
       d= t%10
       s+=d**3
       t//=10
   if i==s:
       print(i,"",end="")
