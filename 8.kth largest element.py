#time: O(n * log(k))
#space: O(k)
# n is the size of the input array and k is the number of largest element that is to be found
#Given an array A of random integers and an integer k, find and return the kth largest element in the array.
#Note: Try to do this question in less than O(N * logN) time.

import heapq

def kth(lst, k):
    minHeap = []
    heapq.heapify(minHeap)
    n = len(lst)
    for i in range(k):
        heapq.heappush(minHeap, lst[i])
    for i in range(k, n):
        if lst[i] > minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, lst[i])
    return minHeap[0]

n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kth(lst, k)
print(ans)
