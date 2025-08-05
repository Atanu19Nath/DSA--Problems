def longest_subarray(arr, sum):

    prefix_sum ={}

    longest = float('-inf')
    
    c_sum = 0
    for i in range(0,len(arr)):

        c_sum = c_sum + arr[i]

        if c_sum == sum:

            longest  = max(longest,i + 1)
            print("first=",longest)

        elif c_sum - sum in prefix_sum:
             
            longest = max(longest, i+1)
            print("second = ",longest)
        
        else:

            prefix_sum[c_sum] = i

      
    return longest

arr = [1,-1,1,1,1,-1,-1]

print(longest_subarray(arr,0))