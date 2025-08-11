def problem(arr,k):
   
    list2 = []

    list1 = []

    start = 0

    maxlength = float('-inf')
    
    for end in range(len(arr)):

            list1.append(arr[end])
   
            if end - start + 1 == k:
    
                maxlength = max(list1)
                list2.append(maxlength)
                 
                if list1[0] == maxlength:
                      
                      maxlength = max(list1)
                  
                list1.pop(0)
                start +=1

    print(list2)        


# arr = [1, 2, 3, 1, 4]
# k = 3

arr = [8, 5, 10, 7, 9, 4, 15, 12]
k = 4

problem(arr,k)