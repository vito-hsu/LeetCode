height = [1,8,6,2,5,4,8,3,7]        # Output: 49
height = [1,1]                      # Output: 1

class Solution:
    def maxArea(self, height):
        start = 0
        end = len(height)-1
        ans = 0
        while start != end:
            if min(height[start], height[end])*(end-start)>ans:
                ans = min(height[start], height[end])*(end-start)
            elif height[start]>height[end]:
                end = end -1
            elif height[start]<height[end]:
                start = start + 1
            elif height[start]==height[end] and end-start>1:
                start += 1
                end -= 1
            elif height[start]==height[end] and end-start==1:
                start += 1
            else:
                assert False, "有錯,請檢察"
        return ans
    
ans = Solution()
ans.maxArea(height=height)