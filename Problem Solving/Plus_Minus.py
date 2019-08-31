
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n=len(arr)
    pos=0
    neg=0
    zero=0
    for i in range(n):
        if arr[i]>0:
            pos+=1;
        elif arr[i]<0:
            neg+=1
        elif arr[i]==0:
            zero+=1
    print(round(pos/n,6))
    print(round(neg/n,6))
    print(round(zero/n,6))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
