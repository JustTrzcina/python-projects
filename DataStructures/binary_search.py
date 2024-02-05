from typing import List

def binary_search(items:List,value:int):
    left, right = 0,len(items)-1

    while left<=right:
        middle = (left+right)//2

        if items[middle]==value:
            return middle
        elif items[middle]<value:
            left = middle+1
        else:
            right = middle-1

    return -1

if __name__ =='__main__':
    print(binary_search([1,1,2,3,5,6,7,8,8,14,33,55,75],55))
