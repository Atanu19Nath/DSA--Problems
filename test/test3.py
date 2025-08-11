def maxfruit(arr):
     


    maxcount = 0

    for i in range(len(arr)):

        set1 = set()

        for j in range(i,len(arr)):

            set1.add(arr[j])
            
            if len(set1) > 2 :
                break
                
            maxcount = max(maxcount,j-i+1)

    print(maxcount)
            
        


arr = [1,2,3,2,2]

maxfruit(arr)