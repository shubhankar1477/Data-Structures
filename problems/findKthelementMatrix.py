from heapq import heappop,heappush

def smallest(m,k):
    n = len(m)
    heap = []
    res = -1
    for i in range(min(k,n)):
        for j in range(min(k,n)):
            heappush(heap,m[i][j])
    for _ in range(k):
        res = heappop(heap)
    return res


item = smallest([[1,4,7],[3,5,9],[6,8,11]],4)
print(item)