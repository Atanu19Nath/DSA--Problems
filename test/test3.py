def problem(arr,a,b):
     

    maxsum = float('-inf') 
    for i in range(len(arr)):

        list1 = []

        csum = 0

        for j in range(i,len(arr)):
             
            csum = csum + arr[j]
            list1.append(arr[j])
            
            if len(list1) >= a and len(list1) <=b:

                maxsum = max(csum,maxsum)
                print(list1)

        print(maxsum)

# arr = [-1, 3 , -1, -2, 5, 3, -5, 2, 2]

# a = 3
# b = 5
arr = [1, 1, -8, 8, 10, -2, 4, 7, -7, 8, 3, 6, -9]
a = 2
b = 6


# arr = [4, 5, -1, -2, 6]
# a = 2
# b = 4
problem(arr,a,b)