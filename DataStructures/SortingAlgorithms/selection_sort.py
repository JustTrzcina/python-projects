'''This module implements selection sort as a part of data structures course exercises'''

from typing import List

def selection_sort(arr:List):
    '''
    Implements selection sort algorithm

    Parameters:
        arr : The input list of integers to be sorted.

    Returns:
        Sorted list
    NOTE: Worst case O(n^2) but minimizes the amount of swaps
    '''
    def swap(arr,idx1,idx2):
        arr[idx1],arr[idx2] = arr[idx2],arr[idx1]

    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        if i!=min_index:
            swap(arr,min_index,i)
            print(f'Swapping: {min_index} to {i}')
    return arr
print(selection_sort([1,2,5,4,5,7,3,2,34,22,11,25]))
