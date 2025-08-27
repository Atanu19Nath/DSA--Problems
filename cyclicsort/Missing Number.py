def missing_number(arr):

    i = 0

    while i < len(arr):

        correct_index = arr[i]

        if arr[i] < len(arr) and arr[i] != arr[correct_index]:

            arr[i],arr[correct_index] = arr[correct_index],arr[i]

        else:

            i +=1
    
    for i in range(len(arr)):

        if i != arr[i]:

            return i
        
arr = [4,0,3,1,2,6,7,8,9,10,12,5]

print(missing_number(arr))


            
