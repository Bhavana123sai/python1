from itertools import combinations
n=int(input())
l=input().split()
k=int(input())
C=list(combinations(l,k))
f=[i for i in C if'a' in i]
print("{0:.3}".format(len(f)/len(C)))
