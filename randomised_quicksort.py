import random

def partition(array, low, high):
    pivot_index = random.randrange(low, high+1)
    array[pivot_index], array[high] = array[high], array[pivot_index]
    j=low-1
    for i in range(low, high):
        if array[i]<=array[high]:
            j=j+1
            array[j], array[i] = array[i], array[j]
    array[high], array[j+1] = array[j+1], array[high]
    return j+1


def randomised_quicksort(array, low, high):

    if low<high:

        p = partition(array, low, high)
        randomised_quicksort(array, low, p-1)
        randomised_quicksort(array, p+1, high)
        


if __name__=="__main__":
    array = [10, 3, 4, 6, 7, 20, 8, 15]
    randomised_quicksort(array, 0, len(array)-1)
    print(f"Sorted array: {array}")