arr = [1,2,3,4,5,10,6,7,8,9] ; k = 5    # Output: true
arr = [1,2,3,4,5,6] ; k = 7             # Output: true
arr = [1,2,3,4,5,6] ; k = 10            # Output: false
arr = [-10,10] ; k = 2                  # 
arr = [3,8,7,2] ; k = 10

arr = [2,3,7,-9,4,4,7,3,2,10,8,15,2,1,-8,10,-5,10,-2,21,9,20,0,4,24,5,12,-10,8,9,18,13,-8,10,-4,-3,0,16,-4,8,14,15,-9,0,0,-6,11,-3,10,11,7,-1,-5,5,11,2,5,9,-2,8,9,-10,6,-2,7,8,3,0,-2,11]
k = 18


import collections

class Solution:
    def canArrange(self, arr, k: int) -> bool:
        key_list    = [num%k for num in arr]
        key_set     = set(key_list)
        key_count   = list(collections.Counter(key_list).items())
        
        for num in range(1,k):
            if num not in key_set:
                key_count.append((num,0))
        key_count.sort()


        try:
            key_count_0 = [count for num, count in key_count if num==0][0]
        except:
            key_count_0 = 0
        
        if key_count_0%2!=0:
            return False

        key_count   = [count for num, count in key_count if num!=0]


        if k%2==1:
            if key_count[:int(len(key_count)/2)]==key_count[len(key_count):int(len(key_count)/2)-1:-1]:
                return True
            else:
                return False
        elif k%2==0:
            if k==2:
                if key_count[0]%2!=0:
                    return False
                else:
                    return True
            else:
                if key_count[int(k/2)-1]%2==1:
                    return False
                elif key_count[:int(len(key_count)/2)]==key_count[len(key_count):int(len(key_count)/2):-1]:
                    return True
                else:
                    return False