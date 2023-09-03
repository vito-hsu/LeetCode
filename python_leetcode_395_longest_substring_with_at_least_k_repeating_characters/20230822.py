s = "aaabb" ; k = 3                 # Output: 3
s = "ababbc" ; k = 2                # Output: 5
s = "ababbcaaacbbbbbbbbb" ; k=3     # Output: 9
s = "weitong" ; k = 2               # Output: 

s = "bababababababababababababababababaabababababaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
k = 30


import collections



class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans_lists = [s]
        final_ans = 0

        while True:
            after_ans_lists = ans_lists
            for ans_list in ans_lists:      # ans_list = ans_lists[0]
                element_counts = collections.Counter(ans_list).most_common()[::-1]
                key_character = element_counts[0][0] if element_counts[0][1]<k else ''
                
                if len(key_character)==0:
                    final_ans = max(len(ans_list), final_ans)
                    print(final_ans)
                else:
                    ans_lists = ans_lists[1:]
                    new_ans_lists = [char for char in ans_list.split(key_character) if len(char)>final_ans]
                    ans_lists.extend(new_ans_lists) 
            
            if after_ans_lists == ans_lists:
                break

        return final_ans