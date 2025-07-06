
def swap(A, sorted_index, i): 
    A[sorted_index], A[i] = A[i], A[sorted_index]

def partition(A, low, high): 

    # pick a pivot (we pick the last element for now)
    pivot = A[high]

    # this index keeps track of all the values lower then the pivot
    sorted_index = low - 1

    # we go trough each element and place it at the start of the array
    # if it is lower then the pivot 
    # Final: We end up with elements lower then the pivot at the start 
    # and elements higher thent the pivot at the end 
    for i in range(low, high): 
        if A[i] < pivot: 
            sorted_index += 1
            swap(A, sorted_index, i)

    # Finally the pivot is swapped such that it is in between the higher
    # and lower part of the array 
    swap(A, sorted_index + 1, high)
    return sorted_index + 1

def qs(A, low, high):
    # if low and high are the same (one element) we simply return 
    if high <= low: 
        return 

    pivot_index = partition(A, low, high)

    qs(A, low, pivot_index - 1)
    qs(A, pivot_index + 1, high)

def quicksort(A): 
    qs(A, 0, len(A) - 1)
