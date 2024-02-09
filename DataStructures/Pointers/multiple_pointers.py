from typing import List

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
    