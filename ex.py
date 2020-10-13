x=int(input("ENTER X"))
y=int(input("ENTER Y"))
z=int(input("ENTER Z"))
n=int(input("ENTER N"))
ans=[[a,b,c] for a in range(0,x+1) for b in range (0,y+1) for c in range (0,z+1)]
s=[]

for i,j,k in ans:
    sum1=i+j+k
    if (sum1!=n):
        s.append([i,j,k])
print(s)    
      
        

