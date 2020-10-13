def fibnocii(n):
    l=[]
    a=-1
    b=1
    c=0
    for i in range(n):
        a=b
        b=c
        c=a+b
        l.append(c)
    if n in l:
        print("")
    else:
        print("no")
n=fibnocii(int(input()))


     
        


    


            
  
