#s=str(input())
#print(s.strip())
import re
s=str(input())
print(re.sub("\s+"," ",s))

