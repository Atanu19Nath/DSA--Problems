from collections import deque

def counter(arr, a, b):
    start = 0
    maxsum = float('-inf')
    csum = 0
    window = deque()

    for end in range(len(arr)):
        csum += arr[end]
        window.append(arr[end])

        # shrink if window size exceeds b
        while end - start + 1 > b:
            csum -= arr[start]
            window.popleft()
            start += 1

        # check only if window size is between a and b
        if a <= end - start + 1 <= b:
            maxsum = max(maxsum, csum)
            print(list(window), "sum:", csum, "max:", maxsum)

    print("Final max sum:", maxsum)



# arr = [-1, 3 , -1, -2, 5, 3, -5, 2, 2]

# a = 3
# b = 5

arr = [1, 1, -8, 8, 10, -2, 4, 7, -7, 8, 3, 6, -9]
a = 2
b = 6

counter(arr,a,b)