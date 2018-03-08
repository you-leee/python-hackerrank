from heapq import heappush, heappop

addHeap = []
remHeap = []
q = int(input().strip())
for i in range(q):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        heappush(addHeap,arr[1])
    elif arr[0] == 2:
        heappush(remHeap, arr[1])
    else:
        while len(remHeap) > 0 and remHeap[0] == addHeap[0]:
            heappop(remHeap)
            heappop(addHeap)
        print(addHeap[0])
