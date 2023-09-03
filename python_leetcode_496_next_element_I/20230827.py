nums1 = [4,1,2] ; nums2 = [1,3,4,2]      # Output: [-1,3,-1]
nums1 = [2,4] ; nums2 = [1,2,3,4]        # Output: [3,-1]


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        key_set = set(nums2)
        ans_list = []
        
        for num in nums1:
            if num in key_set:
                key_ind = nums2.index(num)
                if num == nums2[-1]:
                    ans_list.append(-1)
                for num2 in nums2[key_ind+1:]:
                    if num2>num:
                        ans_list.append(num2)
                        break
                    elif num2 == nums2[-1]:
                        ans_list.append(-1)
            else:
                ans_list.append(-1)
        return ans_list
