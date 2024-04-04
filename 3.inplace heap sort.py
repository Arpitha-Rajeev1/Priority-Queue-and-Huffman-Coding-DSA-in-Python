def down_heapify(arr, i, n):
    parentIndex = i
    leftChildIndex = 2 * parentIndex + 1
    rightChildIndex = 2 * parentIndex + 2

    while leftChildIndex < n:
        minIndex = parentIndex
        if arr[minIndex] > arr[leftChildIndex]:
            minIndex = leftChildIndex
        if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
            minIndex = rightChildIndex
        if minIndex == parentIndex:
            return
        arr[minIndex], arr[parentIndex] = arr[parentIndex], arr[minIndex]
        parentIndex = minIndex
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 1
    return  

def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        down_heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        down_heapify(arr, 0, i)
    return

arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele, end = ' ')
    

#extra edge cases
def Heapify(arr,i,n):
    parentIndex=i
    leftchildindex=2*parentIndex+1
    rightchildindex=2*parentIndex+2

    while leftchildindex<n:
        minindex=parentIndex
        if arr[minindex]>arr[leftchildindex]:
            minindex=leftchildindex
        if rightchildindex<n and arr[minindex]>arr[rightchildindex]:
            minindex=rightchildindex
        if minindex==parentIndex:
            return
        arr[minindex],arr[parentIndex]=arr[parentIndex],arr[minindex]
        parentIndex=minindex
        leftchildindex=2*parentIndex+1
        rightchildindex=2*parentIndex+2
    return

def heapSort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        Heapify(arr,i,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        Heapify(arr,0,i)
    return
        
    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i-1]=arr[i-1],arr[0]
        downheapify(arr,i,0)

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele,end=' ')
