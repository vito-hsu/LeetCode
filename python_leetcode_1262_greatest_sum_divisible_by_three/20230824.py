nums = [3,6,5,1,8]  # Output: 18
nums = [4]          # Output: 0
nums = [1,2,3,4,4]  # Output: 12
nums = [1,1,3]      # 


class Solution:
    def maxSumDivThree(self, nums) -> int:
        total_sum   = sum(nums)
        key_num     = total_sum%3

        if key_num%3== 0:
            print(total_sum)# return total_sum
        
        nums.sort()

        key_list1 = []
        key_list2 = []
        if key_num  == 1:
            for num in nums:
                if num%3 == 2:
                    key_list2.append(num)
                    if num>sum(key_list2[:2]):
                        print(total_sum-sum(key_list2[:2]))#return total_sum-sum(key_list2[:2])
                elif num%3 == 1:
                    if len(key_list2)<2 or num<sum(key_list2[:2]):
                        print(total_sum-num)#return total_sum-num
                    else:
                        print(total_sum-sum(key_list2[:2]))#return total_sum-sum(key_list2[:2])                    
            return total_sum-sum(key_list2[:2])
        elif key_num == 2:
            for num in nums:
                if num%3 == 2:
                    if len(key_list1)<2 or num<sum(key_list1[:2]):
                        print(total_sum-num)#return total_sum-num
                    else:
                        print(total_sum-sum(key_list1[:2]))#return total_sum-sum(key_list1[:2])
                elif num%3 == 1:
                    key_list1.append(num)
                    if num>sum(key_list1[:2]):
                        print(total_sum-sum(key_list1[:2]))#return total_sum-sum(key_list1[:2])
            return total_sum-sum(key_list1[:2])


