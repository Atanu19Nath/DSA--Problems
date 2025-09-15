def helper(arr,start,end):
    
    
    print("helper1")
    
    n = len(arr)
    
    ans = -1
    
    while start <=end:       
        
        mid = start + ( end - start )//2
        
        pre = (mid + n - 1) % n

        next = (mid + 1) % n
        
        print(pre,mid,next)
    
        if arr[pre] != arr[mid] and arr[mid] != arr[next]:

            ans = arr[mid]  
            
        end = mid - 1
        
    return ans
        
def helper2(arr,start,end):
    
    n = len(arr)
    
    ans = -1
    
    print("helper2")
    
    while start <=end:
        
        
        
        mid = start + ( end - start )//2
        
        pre = (mid + n - 1) % n

        next = (mid + 1) % n
        
        print(pre,mid,next)

        if arr[pre] != arr[mid] and arr[mid] != arr[next]:

            ans = arr[mid]            
        
        start = mid + 1
        
    return ans



def singleNonDuplicate(arr):

    start = 0

    end = len(arr) -1

    n = len(arr)

    mid = start + ( end - start )//2

    pre = (mid + n - 1) % n

    next = (mid + 1) % n
    
    print(pre,mid,next)
    

    if arr[pre] != arr[mid] and arr[mid] != arr[next]:

        return arr[mid]
    
    else:
        print("else")
        ans1 = helper(arr,start, pre)
        
        print("ans1 = ",ans1)
        
        if ans1 != -1:
            
            return ans1
        
        ans2 = helper2(arr,next,end)
        
        if ans2 !=-1:
            
            return ans2
        
    return -1

nums = [1,1,2,3,3,4,4,8,8]


print(nums)

print(singleNonDuplicate(nums))