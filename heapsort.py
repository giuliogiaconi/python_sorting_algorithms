"Python implementation of the heapsort algorithm"


def max_heapify(arr, N, i):
    l = (i*2) + 1 # left child
    r = (i*2) + 2 # right child
    largest = i # initialise largest as root

    if l<N and arr[l] > arr[i]: # compare root with left child
        largest = l
    
    if r<N and arr[r] > arr[largest]: # compare root with right child
        largest = r

    if largest !=i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, N, largest) # heapify the current largest element


def heapsort(arr):
    l = len(arr)
    for i in range(l//2-1, -1, -1):
        max_heapify(arr, l, i)
        arr[i], arr[0] = arr[0], arr[i]

    for i in range(l-1, 0, -1): # extract elements
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


if __name__=="__main__":
    test_arr = [10,5,4,7,2,3,8]
    print(f"original array: {test_arr}")
    heapsort(test_arr)
    print(f"Sorted array: {test_arr}")