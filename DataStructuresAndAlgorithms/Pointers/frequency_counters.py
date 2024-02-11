'''Module for implementation of frequency counters '''

from typing import List
from timeit import timeit
from copy import deepcopy

list_1=[3, 17, 10, 9, 12, 6, 14, 8, 1, 5, 16, 20, 18, 4, 11, 7, 15, 13, 2, 19]
list_2=[9, 289, 100, 81, 144, 36, 196, 64, 1, 25, 256, 400, 324, 16, 121, 49, 225, 169, 4, 361]

def same_naive(arr1:List,arr2:List):
    '''
        Returns true if every value in the array has it's
        corresponding values squared in the second array
        using naive method
    '''
    if len(arr1) != len(arr2):
        return False

    for num in arr1:
        try:
            index = arr2.index(num**2)
        except ValueError:
            return False
        del arr2[index]
    return True

execution_time = timeit(lambda:same_naive(arr1=deepcopy(list_1),arr2=deepcopy(list_2)),number=10)
print(execution_time)

def same(arr1:List,arr2:List):
    '''
        Returns true if every value in the array has it's
        corresponding values squared in the second array
        using frequency pattern method
    '''
    if len(arr1) != len(arr2):
        return False

    frequency_counter_1={}
    frequency_counter_2={}
    for value in arr1:
        frequency_counter_1[value]=frequency_counter_1.get(value,0) + 1
    for value in arr2:
        frequency_counter_2[value]=frequency_counter_2.get(value,0) + 1

    for key,value in frequency_counter_1.items():
        if not key**2 in frequency_counter_2:
            (print(key,value))
            return False
        if frequency_counter_2[key**2]!= value:
            (print(key,value))
            return False
    return True

execution_time = timeit(lambda:same(arr1=deepcopy(list_1),arr2=deepcopy(list_2)),number=10)
print(execution_time)

def is_anagram(entry_1:str,entry_2:str):
    '''
        Checks if two given strings are anagrams
        using the frequency pattern method
    '''
    char_freq_1={}
    char_freq_2={}
    for character in entry_1:
        char_freq_1[character] = char_freq_1.get(character,0)+1

    for character in entry_2:
        char_freq_2[character] = char_freq_2.get(character,0)+1

    for char,freq in char_freq_1.items():
        if not char in char_freq_2:
            return False
        if char_freq_2[char] != freq:
            return False
    return True

print(is_anagram(' ',' '))

def is_anagram_streamlined(entry_1:str,entry_2:str):
    '''
        Checks if two given strings are anagrams
        using the frequency pattern method
    '''
    char_freq_1={}
    for character in entry_1:
        char_freq_1[character] = char_freq_1.get(character,0)+1

    for char in entry_2:
        if not char_freq_1[char]:
            return False
        char_freq_1[char]-=1

    return True

print(is_anagram_streamlined('chujjj','juhcccccc'))
