import heapq

nums = [(5,'a'),(3,'b'),(8,'c'),(1,'d')]

heapq.heapify(nums)
heapq.heappush(nums,(4,'e'))   # converts list into a min-heap
print(nums)

heapq.heappush(nums,(10,'t'))

print(nums)

ans = heapq.heappop(nums)

print(ans)