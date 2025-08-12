def problem(arr,k):

    count = 0
    
    for i in range(len(arr)):

        list1 = []

        product = 1

        for j in range(i,len(arr)):

            product = product * arr[j]

            list1.append(arr[j])    
            
            if product <=k:
                count = count + 1
                print(list1)

    print(count)



# arr = [1, 9, 2, 8, 6, 4, 3]

# k =100

k = 10
arr = [1, 2, 3, 4]

problem(arr,k)