import random

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

def check_if_add_at_the_position(position):
    ans1 = 0
    ans2 = 0
    for i in range(position):
        if height[position]<height[i]:
            ans1 = 1        #  print(f'add at {i}')
            break
    for j in range(position+1, len(height)):
        if height[position]<height[j]:
            ans2 = 1        #  print(f'add at {j}')
            break
    return True if ans1*ans2==1 else False

iters = len(height)*5*(max(height)-min(height))

def bulid_complete(height):
    add_num = 0
    for _ in range(iters):
        ran_num = random.randint(0,(len(height)-1)) # position=ran_num
        if check_if_add_at_the_position(position=ran_num)== True:
            height[ran_num] += 1
            add_num += 1
    return add_num




















def check_if_add_at_the_position(position, height):
    ans1 = 0
    ans2 = 0
    for i in range(position):
        if height[position]<height[i]:
            ans1 = 1        #  print(f'add at {i}')
            break
    for j in range(position+1, len(height)):
        if height[position]<height[j]:
            ans2 = 1        #  print(f'add at {j}')
            break
    return True if ans1*ans2==1 else False

def bulid_complete(height, iters):
    add_num = 0
    for _ in range(iters):
        ran_num = random.randint(0,(len(height)-1)) # position=ran_num
        if check_if_add_at_the_position(position=ran_num, height=height)== True:
            height[ran_num] += 1
            add_num += 1
    return add_num


class Solution:
    def trap(self, height):
        iters = len(height)*5*(max(height)-min(height))
        ans = bulid_complete(height, iters)
        return ans
    
a = Solution()
a.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

