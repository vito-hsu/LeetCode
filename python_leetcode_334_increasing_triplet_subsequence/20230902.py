nums = [1,2,3,4,5]      # Output: true
nums = [2,1,5,0,4,6]    # Output: true
nums = [2,1,5,0,6]    # Output: true

class Solution:
    def increasingTriplet(self, nums) -> bool:
        num1 = 99999999999999999
        num2 = 99999999999999999
        num3 = 99999999999999999
        
        for ind, num in enumerate(nums):
            if num<num1:
                num1 = num
            
            if num<num2 and num>num1:
                num2 = num

            if num<num3 and num>num2:
                num3 = num

        if num3!=99999999999999999:
            return True
        else:
            return False
            