def get_smallest(arr):    
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1,len(arr)):
        if arr[i]< smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

def selection_sort(arr):
    result = []
    for i in range(len(arr)):
        smallest = get_smallest(arr)
        result.append(arr.pop(smallest))
    return result

print(selection_sort([12,90,1,0]))

assert selection_sort([12,90,1,0]) == [0,1,12,90]
assert selection_sort([14,92,0,0]) == [0,0,14,92]