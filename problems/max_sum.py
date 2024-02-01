def max_sum(array):
    n = len(array)
    max_sum = array[0]
    curr_sum = 0
    for i in range(n):
        curr_sum += array[i]
        max_sum = max(max_sum,curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum
    
maxsum = max_sum([-1,-3,5,-4,3,-6,9,2])
print(maxsum)