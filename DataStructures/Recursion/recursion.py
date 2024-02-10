'''Explains basics of recursion'''

from typing import List

def count_down(num:int):
    '''
        Counts down using tail recursion
    '''
    print(num)
    if num==0:
        return
    count_down(num-1)

count_down(num=20)

def sum_range(num:int):
    '''
        Sums the values in given range recursively
    '''
    if num==1:
        return 1
    return num+(sum_range(num-1))

print(sum_range(5))

def factorial(num:int):
    '''
        Recursive factorial implementation
    '''
    if num == 1:
        return 1
    return num * factorial(num-1)

def factorial_tail(num:int, _result:int=1):
    '''
       Tail recursive factorial implementation
    '''
    if num==0:
        return 1
    if num-1 == 0:
        return _result
    return factorial_tail(num-1,_result *num)

print(factorial_tail(0))

def collect_even_values(arr:List[int]):
    '''
        Collects all the even values from passed array
        with internal recursive helper
    '''
    result=[]

    def helper(helper_arr):
        if len(helper_arr) == 0:
            return
        if helper_arr[0]%2==0:
            result.append(helper_arr[0])
        helper(helper_arr[1:])

    helper(arr)
    return result

print(collect_even_values([1,2,3,4,5,6,7,8,9,10]))

#  NOTE: Aparently Python does not optimize the tail recursion!

def power_operation(base:int,exponent:int):
    '''
        Implements recursive power operator
    '''
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    return base * power_operation(base,exponent-1)

print(power_operation(2,6))

def product_of_array(arr:List[int]):
    '''
        Implements multiplication of array items recursively
    '''
    if len(arr)==0:
        return 1
    if arr[0] == 0:
        raise ValueError('Zero detected in the array')
    return arr[0]*product_of_array(arr[1:])

print(product_of_array([1,2,3,10]))

def fibonacci(n:int):
    '''
        Implements recursive fibonacci
    '''
    if n <=2 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def string_reverse(string:str):
    '''
        Implements recursive string reversal
    '''
    if len(string)==1:
        return string
    return string[-1]+string_reverse(string[:-1])

print(string_reverse('recursion'))

def is_palindrome(string:str):
    '''
        Implements recursive palindrom search
    '''
    if len(string)<=1:
        return True

    if string[0]==string[-1]:
        return is_palindrome(string[1:-1])
    return False

print(is_palindrome('amanaplanacanalpanama'))
