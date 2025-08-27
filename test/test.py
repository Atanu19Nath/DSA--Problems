def merge(arr):

    arr.sort()

    ans = []

    for i in range(len(arr)):
       
        if not ans:
            ans.append(arr[i])
            
        elif arr[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
        else:
            ans.append(arr[i])

    return ans


# arr = [[1, 3], [2, 4],[9, 10],[6, 8]]
arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
# arr = [[1, 2], [2, 3]]

print(merge(arr))