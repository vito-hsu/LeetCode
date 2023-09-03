nums1 = [1,2,2,1] ; nums2 = [2,2]               # [2,2]
nums1 = [4,9,5] ; nums2 = [9,4,9,8,4]           # [4,9]
nums1 = [1,2,2,1] ; nums2 = [2]                 # [2]

class Solution:
    def intersect(self, nums1, nums2):
        nums11 = [num for num in nums1 if 350>num>=0    ]
        nums12 = [num for num in nums1 if 700>num>=350  ]
        nums13 = [num for num in nums1 if num>=700      ]

        nums21 = [num for num in nums2 if 350>num>=0    ]
        nums22 = [num for num in nums2 if 700>num>=350  ]
        nums23 = [num for num in nums2 if num>=700      ]

        ans_list = []
        for num in nums11:
            if num in nums21:
                nums21.remove(num)
                ans_list.append(num)

        for num in nums12:
            if num in nums22:
                nums22.remove(num)
                ans_list.append(num)

        for num in nums13:
            if num in nums23:
                nums23.remove(num)
                ans_list.append(num)

        
        return ans_list