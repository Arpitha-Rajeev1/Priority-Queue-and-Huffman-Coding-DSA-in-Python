def checkMaxHeap(arr, n):

    for i in range(((n - 2) // 2) + 1):
        if arr[2*i + 1] > arr[i]:
            return 0
        if (2*i + 2 < n and arr[2*i+2] > arr[i]):
            return 0
    return 1


n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst, n) else print('false')

#another solution
#time: O(n)
#space: O(1)
def check(lst):
    n = len(lst)
    for i in range(n):
        left = (2 * i) + 1
        right = left + 1
        if left < n and lst[left] > lst[i]:
            return False
        if right < n and lst[right] > lst[i]:
            return False
    return True


