from collections import Counter

class Solution:
    def search(self, arr, txt):
        i = 0
        j = 0
        k = len(txt)
        size = len(arr)

        txt_count = Counter(txt)
        window = Counter()

        while j < size:
            

            # step 1. calculation 
            window[arr[j]] += 1

            if j - i + 1 < k:
                
                j += 1

             
            elif j - i + 1 == k:

            # step 2. get ans from calculation ( when it hit the condition)
                
                if window == txt_count:
                    
                    return True
            # step 3. removing left side element        
                window[arr[i]] -= 1
                
                if window[arr[i]] == 0:
                    
                    del window[arr[i]]
                    
                i += 1
                j += 1

        return False

s = Solution()

print(s.search("geeks","eek"))