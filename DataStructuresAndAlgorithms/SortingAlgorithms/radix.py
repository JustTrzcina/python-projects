'''This module implements radix as a part of data structures course exercises'''

from typing import List
from math import floor,log10
from itertools import chain

def get_digit(number:int,position:int)->int:
    '''
    Helper function originally designed for radix sort.
    Function is supposed to give back the digit at a certain
    position in the number.

    Parameters:
        number : A number in which a certain position is to be read
        position : Indicates the position in the number

    Returns:
        Returns a digit at a certain position in a number       
    '''
    return floor(abs(number)/pow(10,position)) % 10

def digits_in_number(number:int):
    '''
    Checks how many digits a number has.

    Parameters:
        number : Number whose digits will be counted
    
    Returns:
        Amount of digits in the specified number
    '''
    if number==0:
        return 1
    return floor(log10(abs(number)))+1

def most_digits(arr:List[int]):
    '''
    Given an array of numbers returns the number of digits
    in the largest numbers in the list

    Parameters:
        arr : List of numbers to be checked
    
    Returns:
        Most amount of digits in a single number
    '''
    max_digits = 0
    for number in arr:
        max_digits=max(max_digits,digits_in_number(number))
    return max_digits


def radix_sort(arr:List[int])->List[int]:
    '''
    Implements radix sort algorithm

    Parameters:
        arr : List of integers to be sorted

    Returns:
        List of sorted integers

    NOTE: Average time complexity of O(nk) where:
        n - amount of sorted numbers
        k - max length of singular number
        In some cases it is worth investigating due to the
        fact that k can be logn therefore giving n*logn
    '''
    max_digit_count = most_digits(arr)
    for i in range(max_digit_count):
        digit_buckets = [[] for i in range(10)]
        for number in (arr):
            bucket_index = get_digit(number,i)
            digit_buckets[bucket_index].append(number)
        arr = list(chain(*digit_buckets))
    return arr

print(radix_sort([23,54,235,4632,23,12345,2,3,423]))
