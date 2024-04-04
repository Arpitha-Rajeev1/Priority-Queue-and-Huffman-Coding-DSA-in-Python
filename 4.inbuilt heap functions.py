import heapq

#inbuilt min heap
li = [1, 5, 4, 8, 7, 9, 11]
heapq.heapify(li)
print(li)
heapq.heappush(li, 2)
print(li)
heapq.heappop(li)
print(li)
heapq.heapreplace(li, 6)
print(li)

#inbuilt max heap
heapq._heapify_max(li)
print(li)

print(heapq._heappop_max(li))

print(li)

heapq._heapreplace_max(li, 0)
print(li)

li.append(6)
heapq._siftdown_max(li, 0, len(li) - 1)
print(li)
