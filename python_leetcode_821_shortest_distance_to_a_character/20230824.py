s = "loveleetcode" ; c = "e"    # Output: [3,2,1,0,1,0,0,1,2,2,1,0]



class Solution:
    def shortestToChar(self, s: str, c: str):
        ans_list = []
        key_string = ''
        for _ in range(len(s)):
            try:
                index1 = s.index(c)
            except:
                index1 = 9999999999999999999


            try:
                index2 = key_string.index(c)+1      # notice
            except:
                index2 = 9999999999999999999
            
            ans_list.append(min(index1, index2))
            # print(ans_list)

            key_string = s[0] + key_string
            s = s[1:]
        return ans_list

