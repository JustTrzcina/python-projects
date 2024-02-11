'''This module implements merge sort as a part of data structures course exercises'''

from typing import List

def array_merge(arr_1:List[int],arr_2:List[int]):
    '''
    Merges two sorted lists of type 'int' into one sorted list

    Parameters:
        arr_1 : List of integers representing one side of the array.
        arr_2 : List of integers representing second side of the array.

    Returns: sorted merged list
    '''
    result=[]
    i=0
    j=0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            result.append(arr_1[i])
            i+=1
        else:
            result.append(arr_2[j])
            j+=1
    if i < len(arr_1):
        result.extend(arr_1[i:])
    if j < len(arr_2):
        result.extend(arr_2[j:])

    return result

def merge_sort(arr:List[int]):
    '''
    Implements merge sort algorithm on a list of integers
   
    Parameters:
        arr: List of integers to be sorted
    
    Returns: sorted list

    NOTE: O(n*logn)
    '''
    if len(arr)<=1 :
        return arr
    arr_left = merge_sort(arr[:len(arr)//2])
    arr_right = merge_sort(arr[len(arr)//2:])
    return array_merge(arr_left,arr_right)

print(array_merge([1,3,5,90],[2,4,6,7,8,9,10]))
print(merge_sort([1,35,6,3,2,6,34,22,11]))
