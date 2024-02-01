import heapq


k = 5

a = [13,5,2,6,10,9,7,4,3]
heapq.heapify(a)
print(heapq.nlargest(6,a))
