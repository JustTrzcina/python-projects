'''This module implements bubble sort as a part of data structures course exercises'''

from typing import List

def bubble_sort(arr:List):
    '''
    Implements bubble sort algorithm

    Parameters:
        arr : The input list of integers to be sorted.

    Returns: sorted list

    NOTE: O(n) best possible if data nearly 
    sorted, worst case O(n^2)
    '''
    def swap(arr,idx1,idx2):
        arr[idx1],arr[idx2] = arr[idx2],arr[idx1]

    for i in range(len(arr)-1,0,-1):
        no_swaps = True
        for j in range(i):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
                no_swaps = False
        if no_swaps:break
    return arr
print(bubble_sort([1,5,4,2,4,6,7,8,4,3]))
