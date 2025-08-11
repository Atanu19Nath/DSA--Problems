def maxfruit(arr):

    maxcount = 0
    start  = 0
    basket = {}
    for end in range(len(arr)):
            

            if arr[end] in basket:
                 
                 basket[arr[end]] +=1

            if arr[end] not in basket:

                basket[arr[end]] = 1             
            
            while len(basket) > 2 :

                basket[arr[start]] -=1

                if basket[arr[start]]  == 0:
                     
                     del basket[arr[start]]

                start +=1
            
            maxcount = max(maxcount,end - start +1 )
                

    print(maxcount)
            
        

arr = [1,2,3,2,2]

maxfruit(arr)





# BRUTE FORCE APPROACH

# def maxfruit(arr):
     
#     maxcount = 0

#     for i in range(len(arr)):

#         set1 = set()

#         for j in range(i,len(arr)):

#             set1.add(arr[j])
            
#             if len(set1) > 2 :
#                 break
                
#             maxcount = max(maxcount,j-i+1)

#     print(maxcount)
            
        


# arr = [1,2,3,2,2]

# maxfruit(arr)