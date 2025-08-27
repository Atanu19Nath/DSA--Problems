def missing_number(arr):

    i = 0

    while i < len(arr):

        correct_index = arr[i]

        if arr[i] < len(arr) and arr[i] != arr[correct_index]:

            arr[i],arr[correct_index] = arr[correct_index],arr[i]

        else:

            i +=1

    print(arr)

    missing_num = []
    for i in range(len(arr)):

        if i != arr[i]:

            missing_num.append(i)
   
    max_val = max(arr)

    for i in range(len(arr),max_val):

        if i not in arr:

            missing_num.append(i)
    
    
    return missing_num
        
arr = [4,0,3,1,2,6,7,8,9,10,12,13,15,16]

print(missing_number(arr))


            
