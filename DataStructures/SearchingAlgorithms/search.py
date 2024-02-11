'''Module implements search algorithms'''

from typing import List

def linear_search(arr:List,target):
    '''
        Linear search implementation
    '''
    for index,item in enumerate(arr):
        if item == target:
            return index
    return -1

print(linear_search([1,2,3,4,5,6,7,8,9],6))

def binary_search(arr:List[int],target):
    '''
        Implements binary search
        NOTE: works only on sorted arrayss
    '''
    left = 0
    right = len(arr)-1
    middle = (left+right)//2
    while arr[middle]!=target and left <= right:
        if arr[middle] < target:
            left = middle+1
        else:
            right = middle-1
        middle = (left+right)//2
    if arr[middle]==target:
        return middle
    return -1

print(binary_search([2,5,6,8,13,16,22,25,27,30],22))
