# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 18:57:39 2022

@author: heib6
"""

import numpy as np

# Dynamic programming Python implementation
# of LIS problem
 
# lis returns length of the longest
# increasing subsequence in arr of size n
 
 
def lis(arr):
    n = len(arr)
 
    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1]*n
 
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
 
    # Initialize maximum to 0 to get
    # the maximum of all LIS
    maximum = 0
 
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])
 
    return maximum
# end of lis function
 
def get_random_sample_permutation(n,m):
  i=0
  sample=[]
  while i < m:
    item=np.random.permutation(n)
    sample.append(item)
    i+=1
  return sample


def main():
    n=2048
    m=100
    print("get samples")
    sample=get_random_sample_permutation(n,m)
    sum_LIS=0
    print("running algorithm")
    for perm in sample:
        sum_LIS=sum_LIS+lis(perm)
    ave_LIS=sum_LIS//m
    print("average is")
    print(ave_LIS)

if __name__ == "__main__":
    main()

