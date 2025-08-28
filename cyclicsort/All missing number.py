def missing_number(arr):

    i = 0

    while i < len(arr):

        correct_index = arr[i] -1 

        if arr[i] < len(arr) and arr[i] != arr[correct_index]:

            arr[i],arr[correct_index] = arr[correct_index],arr[i]

        else:

            i +=1

    print(arr)

    missing = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            missing.append(i + 1)

    return missing
    # max_val = max(arr)

    # for i in range(len(arr),max_val):

    #     if i not in arr:

    #         missing_num.append(i)
    
    
    return missing_num
        
arr = [4,3,2,7,8,2,3,1]

print(missing_number(arr))


            
