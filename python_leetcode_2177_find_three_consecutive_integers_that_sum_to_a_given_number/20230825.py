num = 33        # Output: [10,11,12]

class Solution:
    def sumOfThree(self, num: int):
        if num==0:
            return [-1,0,1]
        
        if num==3:
            return [0,1,2]

        if num<6:
            return []

        if num%3==0:
            return [int(num/3)-1,int(num/3),int(num/3)+1]
        else:
            return []