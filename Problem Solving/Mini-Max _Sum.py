import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    L=len(arr)
    mini=sum(arr[0:L-1])
    maxi=sum(arr[1: ])
    print(mini,end=" ")
    print(maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
