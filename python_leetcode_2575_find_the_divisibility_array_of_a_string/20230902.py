word = "998244353" ; m = 3           # Output: [1,1,0,0,0,1,1,0,0]



# import sys
# sys.set_int_max_str_digits()




class Solution:
    def divisibilityArray(self, word: str, m: int):
        try:
            ans_list = []
            key_stop = 0
            for i,n in enumerate(word):     # i = 0 ; n = word[i]
                key_num = int(word[key_stop:i+1])
                if key_num%m == 0:
                    ans_list.append(1)
                    key_stop = i+1
                else:
                    ans_list.append(0)
            return ans_list
        except:
            return [0]*len(word)


