import heapq as hq


def kLargest(arr, k):
    minHeap = []
    size = len(arr)
    for i in range(k):
        minHeap.append(arr[i])
    hq.heapify(minHeap)

    for i in range(k, size):
        if minHeap[0] > arr[i]:
            continue
        else:
            minHeap[0] = minHeap[-1]
            minHeap.pop()
            minHeap.append(arr[i])
            hq.heapify(minHeap)

    return minHeap


n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
