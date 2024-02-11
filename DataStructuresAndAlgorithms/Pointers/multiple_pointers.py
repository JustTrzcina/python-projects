'''Module for implementation of multiple pointers approach '''

from typing import List,Tuple
from collections import Counter

def fin_sum_zero_naive(arr_1:List[int]):
    '''
        Searches for a pair of numbers in sorted array
        which sum returns 0. Naive implementation of O(n^2)
    '''
    for i in arr_1:
        for j in range(1,len(arr_1)):
            if i + arr_1[j] == 0:
                return [i,arr_1[j]]
    return 'No matches found'
print(fin_sum_zero_naive([-4,-3,-2,-1,0,1,2,4]))

def fin_sum_zero(arr_1:List[int]):
    '''
        Searches for a pair of numbers in sorted array
        which sum returns 0. Implementation of O(n)
    '''
    left = 0
    right = len(arr_1)-1

    while left < right:
        sum_value = arr_1[left] + arr_1[right]
        if sum_value == 0:
            return [arr_1[left],arr_1[right]]
        if sum_value > 0:
            right -= 1
        else:
            left += 1
    return 'No matches found'

print(fin_sum_zero([-4,-3,-2,-1,0,1,2,3]))

def count_unique_values(arr:List[int]):
    '''
        Accepts a sorted array and conts the unique
        values in the array using multiple pointers
    '''
    if not arr:
        return 0

    count = 1
    trail = 0
    lead = 1

    while lead < len(arr):
        if arr[trail] != arr[lead]:
            count += 1
            trail += 1
            lead += 1
        else:
            lead += 1

    return count

print(count_unique_values([-4,-3,-2,-1,0,1,2,2,3]))

def max_subarray_sum(arr:List[int],n:int):
    '''
        Finds maximum sum of "n" consecutive elements in array
        using sliding window approach
    '''
    if len(arr)<n or n==0:
        return None
    max_sum = sum(arr[:n])
    temp_sum = max_sum

    for i in range(n,len(arr)):
        temp_sum = temp_sum - arr[i-n] + arr[i]
        max_sum = max(temp_sum,max_sum)
    return max_sum

print(f'Max subarray sum: {max_subarray_sum([3,3,5,6,7,12,4,6,2,4,6,2,4],1)}')

def same_frequency(n1:int,n2:int):
    '''
        Given two positive integers, finds out 
        if the two numbers have the same frequency of digits.
    '''
    lookup={}
    for num in str(n1):
        lookup[num]=lookup.get(num,0)+1

    for num in str(n2):
        if not lookup[num]:
            return False
        lookup[num]-=1
    return True

print(f'Same frequency? {same_frequency(234,234)}')

def are_there_duplicates(*values:Tuple[int]):
    '''
        Checks whether there are any duplicates 
        among the arguments passed in.
    '''
    freq_counter={}
    for val in values:
        if freq_counter.get(val) is None:
            freq_counter[val]=1
        else:
            return True
    return False

print(f'Are there duplicates? {are_there_duplicates(234,3,3,5,64,22)}')

def are_there_duplicates_counter(*values:Tuple[int]):
    '''
        Checks whether there are any duplicates 
        among the arguments passed using Counter class
    '''
    counter = Counter(values)
    return any(count>1 for count in counter.values())

print(f'Are there duplicates? {are_there_duplicates(234,3,5,64,22)}')

def average_pair(arr:List[int],target:int)->bool:
    '''
    Given a sorted array of integers and a target
    average, determine if there is a pair of values
    in the array where the average of the pair 
    equals the target average.
    '''
    left=0
    right=len(arr)-1
    if len(arr)==0:
        return False
    while left<right:
        avg = arr[left]+arr[right]/2
        if avg == target:
            return True
        elif avg < target:
            left+=1
        else:
            right-=1
    return False

print(f'Average target found? {average_pair([1,3,3,5,6,7,10,12,19],8)}')
