'''This module implements insertion sort as a part of data structures course exercises'''

from typing import List

def insertion_sort(arr:List[int]):
    '''
    Implements insertion sort algorithm on a List of integers

    Parameters:
        arr : The input list of integers to be sorted.

    Returns: sorted list

    NOTE: O(n^2) but if data almost sorted, usefull when
    data is coming 'live'
    '''
    for i in range(1,len(arr)):
        current_val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_val
    return arr

print(insertion_sort([1,5,4,2,4,6,7,8,4,3]))
