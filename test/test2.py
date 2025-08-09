def target(arr,target):

    tsum = 0

    start = 0
    
    lenght = 0

    for end in range(len(arr)):

        tsum = tsum + arr[end]

        while tsum > k:

            tsum = tsum - arr[start]

            start -= 1

        
        if tsum == target:

            lenght = max(lenght, end - start + 1)

    print(lenght)
            
# s = Solution()

arr = [6, 3 ,1 ,2 ,10, 10]
k = 12
# print(s.minRemovals(arr,k))        


target(arr,k)



