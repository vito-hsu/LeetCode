nums = [4,1,2,3]        # Output: [2,3,4,1]
nums = [2,1]            # Output: [2,1]

class Solution:
    def sortEvenOdd(self, nums):
        key_list1 = [num for ind, num in enumerate(nums) if ind%2==0]
        key_list2 = [num for ind, num in enumerate(nums) if ind%2==1]
        key_list1.sort()
        key_list2.sort(reverse=True)
        
        ans_list = []
        for ind in range(int(len(nums)/2)):
            ans_list.append(key_list1[ind])
            ans_list.append(key_list2[ind])

        if len(nums)%2==1:
            ans_list.append(key_list1[-1])
        return ans_list