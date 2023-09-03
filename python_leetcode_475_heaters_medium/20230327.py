houses = [1,2,3]    ;   heaters = [2]   # Output: 1
houses = [1,2,3,4]  ;   heaters = [1,4] # Output: 1
houses = [1,5]      ;   heaters = [2]   # Output: 3

f = open('data.txt', 'r')
data = f.read()
data = data.split('\n')         # len(data)
houses = eval(data[0])          # len(houses)
heaters = eval(data[1])         # len(heaters)
f.close()

from numpy import array, abs
from time import time



class Solution:
    def findRadius(self, houses, heaters) -> int:
        start = time()                                                  # def func1(x, i):
        houses = list(set(houses))                                          # return abs(x-i)                                                         
        heaters = list(set(heaters))                                    # key_1 = array([list(map(func1, houses, [i for _ in range(len(houses))])) for i in heaters]) 
        key_1 = array([list(abs(array(houses)-i)) for i in heaters])    # key_1 = np.array([list(map(lambda x:abs(x-i), houses)) for i in heaters])
        key_2 = [min(key_1[:,i]) for i in range(key_1.shape[1])]        # i = 0
        end = time()
        end-start
        return max(key_2)