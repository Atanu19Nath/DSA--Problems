from collections import deque

def sorting(arr):

    ans = deque()

    for i in range(len(arr)):
    
        if len(ans) == 0:

            ans.append(arr[i])

        else:

            if arr[i] > ans[0]:

                ans.appendleft(arr[i])
            else:

                ans.append(arr[i])

    ans.pop(arr[1])

    return ans



arr = [1,3,-1]


print(sorting(arr))