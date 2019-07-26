x=int(input())
if x>1:
    for i in range(2,x//2):
        if x%i==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
