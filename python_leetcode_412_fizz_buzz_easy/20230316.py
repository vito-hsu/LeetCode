n = 3   # Output: ["1","2","Fizz"]
n = 5   # Output: ["1","2","Fizz","4","Buzz"]
n = 15  # Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


class Solution:
    def fizzBuzz(self, n: int):
        ans_list = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans_list.append('FizzBuzz')
            elif i%3==0:
                ans_list.append('Fizz')
            elif i%5==0:
                ans_list.append('Buzz')
            else:
                ans_list.append(str(i))
        return ans_list