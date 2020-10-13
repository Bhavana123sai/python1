import numpy
n,m=map(int,input().split())
my_array=numpy.array([input().split() for i in range(n)], int)
print(my_array.transpose())
print(my_array.flatten())
    
        
