def binarysum(arr,k):
    
    count = 0
    
    for i in range(len(arr)):
         
        sum = arr[i]
        for j in range(i+1,len(arr)):

            sum = sum + arr[j]

            if sum == k:

                count = count + 1

    print(count)
            
            

            


arr = [1,0,1,0,1]

k = 2

binarysum(arr,k)