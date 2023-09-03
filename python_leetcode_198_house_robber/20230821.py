nums = [1,2,3,1]    # Output: 4
nums = [2,7,9,3,1]  # Output: 12
nums = [0]          # Output: 0
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
                    # Output: 3365
nums = [55,72,209,143,216,220,122,115,87,227,220,161,79,230,55,56,56,178,124,88,202,65,102]
                    # Output: 1758
nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
                    # Output: 1630


class Solution:
    def rob(self, nums) -> int:




# from random import random

# class Solution:
#     def rob(self, nums) -> int:
#         if len(nums)==1:
#             return nums[0]

#         key_list            = [False]*len(nums)
#         ans_list            = []
#         before_key_list     = []
#         after_key_list      = []
        
#         # first step
#         for ind, num in enumerate(nums):            # ind = 1
#             if ind == 0:
#                 if num>nums[1]:
#                     key_list[:2] = [True]*2
#                     ans_list.append(num)
#             elif ind == len(nums)-1:
#                 if num>nums[ind-1]:
#                     key_list[-2:] = [True]*2
#                     ans_list.append(num)
#             else:
#                 if num >= nums[ind-1] + nums[ind+1]:
#                     key_list[ind-1:ind+2] = [True]*3
#                     ans_list.append(num)

#         unchanged = False
#         while unchanged == False:
            
#             before_key_list.extend(key_list)
#             # second step
#             for ind, num in enumerate(nums):
#                 if key_list[ind:ind+3]==[True,False,False]:
#                     if nums[ind+1]>nums[ind+2]:
#                         key_list[ind:ind+3]=[True]*3
#                         ans_list.append(nums[ind+1]) ; print(nums[ind+1])
#                 elif key_list[ind:ind+3]==[False,False,True]:
#                     if nums[ind+1]>nums[ind]:
#                         key_list[ind:ind+3]=[True]*3
#                         ans_list.append(nums[ind+1]) ; print(nums[ind+1])
                    
#             # third step 
#             for ind, num in enumerate(nums):        # ind = 0
#                 if ind==0 and key_list[:4]==[False]*4:
#                     if nums[ind]+nums[ind+2]>nums[ind+1]+nums[ind+3]:
#                         key_list[ind:ind+4]=[True]*4
#                         ans_list.append(nums[ind]+nums[ind+2]) ; print(nums[ind]+nums[ind+2])
#                 elif key_list[ind:ind+5]==[True,False,False,False,False]:
#                     if nums[ind+1]+nums[ind+3]>nums[ind+2]+nums[ind+4]:
#                         key_list[ind:ind+5]=[True]*5
#                         ans_list.append(nums[ind+1]+nums[ind+3]) ; print(nums[ind+1]+nums[ind+3])
#                 elif key_list[ind:ind+5]==[False,False,False,False,True] or (ind==len(nums)-5 and key_list[-4:]==[False]*4):
#                     if nums[ind+1]+nums[ind+3]>nums[ind]+nums[ind+2]:
#                         key_list[ind:ind+5]=[True]*5
#                         ans_list.append(nums[ind+1]+nums[ind+3]) ; print(nums[ind+1]+nums[ind+3])

#             after_key_list.extend(key_list)
#             if before_key_list == after_key_list:
#                 unchanged = True
#             else:
#                 unchanged = False
#                 after_key_list = []
#                 before_key_list = []

#         # final step - random select !!!!
#         potential_ans_list = []
#         key_copy = key_list.copy()
#         for _ in range(key_copy.count(False)*5):
#             while False in key_copy:
#                 key_index = key_copy.index(False)
#                 if nums[key_index+1]==True:
#                     potential_ans_list.append(nums[key_index])
#                     key_copy[key_index]=True
#                 else:
#                     ran = random()
#                     if ran>0.5 and nums[key_index+2]==False:
#                         potential_ans_list.append(nums[key_index+1])
#                         key_copy[key_index:key_index+3]=[True]*3
#                     elif ran>0.5:
#                         potential_ans_list.append(nums[key_index+1])
#                         key_copy[key_index:key_index+2]=[True]*2
#                     else:
#                         potential_ans_list.append(nums[key_index])
#                         key_copy[key_index:key_index+2]=[True]*2
#             key_copy = key_list.copy()
                
#         ans_list.append(max(potential_ans_list))

#         return sum(ans_list)
    

                                                                                                                               
# 55+209+216+122+227+161+234+534