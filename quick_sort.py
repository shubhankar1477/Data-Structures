def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
assert quick_sort([1,3,4,5,0,19,6]) == [0,1,3,4,5,6,19]
assert quick_sort([1]) == [1]
