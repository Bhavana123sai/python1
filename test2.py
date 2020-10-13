import math
def abundant(n):
    
    a=0
    for i in range(1,n):
        
        if n%i==0:
            
            a=a+i
        print("a:",a)
            
    if a>n:
        return 1
            
    else:
            return 0
n=int(input())
if(abundant(n)==1):
    print("Abundant Number")
else:
     print("not Abundant Number")

    
