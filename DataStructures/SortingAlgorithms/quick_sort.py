'''This module implements quick sort as a part of data structures course exercises'''

from typing import List

def pivot_helper(arr:List[int], start:int=0, end=None):
    """
    Helper function to choose a pivot element for Quick Sort algorithm.

    Parameters:
        arr : The input list of integers to be sorted.
        start : The starting index of the sublist to consider. Defaults to 0.
        end : The ending index of the sublist to consider.
            Defaults to the length of the array minus 1.

    Returns:
        int : The index of the pivot after partitioning.
    """
    if end is None:
        end = len(arr) - 1

    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    pivot = arr[start]
    swap_idx = start
    for i in range(start+1, end+1):
        if pivot > arr[i]:
            swap_idx += 1
            swap(arr, swap_idx, i)
    swap(arr, start, swap_idx)
    return swap_idx

def quick_sort(arr:List[int]):
    """
    Sorts a list using the Quick Sort algorithm.
        
    Parameters:
        arr: List of integers to be sorted
    
    Returns: sorted list

    NOTE: O(n*logn) on average, O(n^2) worst case
    """
    def _quick_sort(arr, start, end):
        if start < end:
            pivot_index = pivot_helper(arr, start, end)
            _quick_sort(arr, start, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, end)

    _quick_sort(arr, 0, len(arr) - 1)
    return arr

# Example usage:
sorted_arr = quick_sort([1,3,5,6,3,4,6,7,8,9])
print("Sorted array:", sorted_arr)