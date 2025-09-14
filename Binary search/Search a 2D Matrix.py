def find_element(arr,key):
    
    
    row = len(arr)
    
    column = len(arr[0])
    
    
    i = 0
    
    j = column - 1
    
    
    while i >= 0 and i < row and j >= 0 and j < column:
        
        print(arr[i][j])
        
        if arr[i][j] == key :
            
            return True
        
        elif arr[i][j] > key :
            
            
            j -= 1
            
        else:
            
            i +=1
            
    return False
            
    


matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 3

print(find_element(matrix,target))