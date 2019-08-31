# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median
size=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
T=int(len(arr)/2)
if len(arr)%2==0:
    L=arr[:T]
    U=arr[T:]
else:
    L=arr[:T]
    U=arr[T+1:]
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))

