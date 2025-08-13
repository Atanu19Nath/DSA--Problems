def counter(arr,a,b):

    start = 0
        
    maxlen = 0
        
    csum = 0
    list1 = []
    for end in range(len(arr)):
            
        csum = csum + arr[end]
        list1.append(arr[end])
            
            
        while end-start+1 > b:
                
            csum = csum - arr[start]

            list1.pop(0)
                
            start+=1
            
            
        if end-start+1 >= a and end-start+1 <=b:
                
            maxlen = max(maxlen,csum)
            print(list1)
            print(maxlen)
                
                
    print(maxlen)

    
# arr = [1, 1, -8, 8, 10, -2, 4, 7, -7, 8, 3, 6, -9]
# a = 2
# b = 6

arr = [-1, 3 , -1, -2, 5, 3, -5, 2, 2]

a = 3
b = 5

counter(arr,a,b)