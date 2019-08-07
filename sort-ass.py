a=int(input())
no=list(map(int,input().split()))[:a]
b=no.sort()
print(*no,sep=' ')

