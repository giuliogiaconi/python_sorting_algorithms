""" Quick sort using last element in the array as pivot"""

import random

def partition(array, low, high):

    pivot = array[high]
    i = low - 1 # index of highest element in low side

    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[j], array[i] = array[i], array[j]

    array[i+1], array[high] = array[high], array[i+1]

    return i+1

    
def quick_sort(array, low, high):
    if low < high:

        part_index = partition(array, low, high)
        quick_sort(array, low, part_index-1)
        quick_sort(array, part_index+1, high)

if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5, 20, 15]
    quick_sort(array, 0, len(array) - 1)
    
    print(f'Sorted array: {array}')

