def maxLen(arr):
    for i in range (len(arr)):
        if(arr[i]==0):
            arr[i]=-1


    k=0
    sum=0
    length=0
    mp = {}
    for i in range (len(arr)):
            
            sum+=arr[i]

            if(sum==k):
                 
                length=max(length,i+1)
            
            if sum not in mp:
                mp[sum] = i
            
            if sum-k in mp:
            
                length = max (length, i - mp[sum-k]-1 + 1 )
        
    return length

arr = [1,-1,1,1,1,-1,-1]

print(maxLen(arr))
    
