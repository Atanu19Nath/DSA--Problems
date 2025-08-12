def counter(arr,k):
    start = 0

    mp = {}
    
    product = 1

    count = 0

    for end in range(len(arr)):

        product = product * arr[end]

        while product > k:

            product = product/arr[start]

            start +=1
        

        count = count + end - start +1

    print(count)
        
            
            

# arr = [1, 9, 2, 8, 6, 4, 3]

# k =100
k = 10
arr = [1, 2, 3, 4]
counter(arr,k)
            
      
