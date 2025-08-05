def find_subarry(arr,sum):

    prefix_sum = {}

    current_sum = 0
    start = 0
    end  = -1

    for i in range(len(arr)):
        
        current_sum = current_sum + arr[i]

        if current_sum == sum:

            end = i
            break

        if current_sum - sum in prefix_sum:

            start = prefix_sum[current_sum-sum]  + 1
            end = i 
            break

        else:
            prefix_sum[current_sum] = i  
            
    print(start, end)


arr = [10,15,-5,15,-10,5]

find_subarry(arr,5)