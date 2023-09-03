nums1 = [1,2,2,1] ; nums2 = [2,2]       # [2]


class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return [num for num in set1 if num in set2]