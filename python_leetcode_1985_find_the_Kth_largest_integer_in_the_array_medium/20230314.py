nums = ["3","6","7","10"]   ;   k = 4           # Output: "3"
nums = ["2","21","12","1"]  ;   k = 3           # Output: "2"
nums = ["0","0"]            ;   k = 2           # Output: "0"


class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        nums = [int(i) for i in nums]
        nums.sort(reverse=True)
        return str(nums[k-1])