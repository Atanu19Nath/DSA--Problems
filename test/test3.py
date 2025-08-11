def problem(arr,k):
   
    list2 = []

    for i in range(len(arr)):

        list1 = []
        for j in range(i,len(arr)):

            list1.append(arr[j])
   
            if j - i + 1 == k:
                print(list1)
                print(max(list1))
                list2.append(max(list1))

    print(list2)        


arr = [1, 2, 3, 1, 4]
k = 3

problem(arr,k)