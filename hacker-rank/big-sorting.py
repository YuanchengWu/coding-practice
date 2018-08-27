def bigSorting(unsorted):
    shitty_quick_sort(unsorted, 0, len(unsorted) - 1)
    return unsorted

def shitty_quick_sort(arr, low, high):
    if low < high:
        wall = partition(arr, low, high)

        shitty_quick_sort(arr, low, wall - 1)
        shitty_quick_sort(arr, wall + 1, high)

def partition(arr, low, high):
    i = ( low-1 )         # index of smaller element
    pivot = int(arr[high])     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if  int(arr[j]) <= pivot:
        
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


arr = ['6', '31415926535897932384626433832795', '1', '3', '10', '3', '5']
# arr = [5, 6, 3, 9]
print(bigSorting(arr))