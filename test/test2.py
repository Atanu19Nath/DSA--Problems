def merge(arr,interval):

    arr.sort()

    ans = []

    for i in range(len(arr)):
       
        if not ans:
            ans.append(arr[i])
        
        elif interval[0] <= ans[-1][1]:

            ans[-1][1] = max(ans[-1][1],interval[1])
            
        elif arr[i][0] <= ans[-1][1]:

            ans[-1][1] = max(ans[-1][1], arr[i][1])
            
        else:
            ans.append(arr[i])

    return ans



arr = [[1,2],[3,5],[6,7],[8,10],[12,16]]

interval = [4,8]

print(merge(arr,interval))