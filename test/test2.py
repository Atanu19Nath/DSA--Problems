def binarysum(arr,k):
    
    count = 0
    csum = 0

    prefix = {}

       
    for j in range(len(arr)):


        csum = csum + arr[j]

        if csum == k:

            count +=1

        if csum - k in prefix:
            
            count = count + prefix[csum-k]

        if csum in prefix:

            prefix[csum] +=1
        
        if csum not in prefix:

            prefix[csum] = 1

        
        
    print(count)

arr = [1,0,1,0,1]

k = 2

binarysum(arr,k)