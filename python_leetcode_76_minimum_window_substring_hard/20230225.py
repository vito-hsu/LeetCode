import random

s = "ADOBECODEBANC"
t = "ABC"

s = "a"
t = "a"

s = "a"
t = "aa"            

s = "a"
t = "b"


s = "caacbabbbcacbabaabcbbbcbbcbbbbbbabbcacbbcbabccbabbc"
t = "bababbcabccccbabbacacb"
true = "caacbabbbcacbabaabcbbbcbbc"


s = "wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon"
t = "ozgzyywxvtublcl"
true = "tcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanl"





def s_in_t(s, t):
    s1 = list(s)
    t1 = list(t)
    try:
        for i in range(len(t1)):
            s1.remove(t1[i])  
        return True
    except:
        return False


list1 = []
for index, element in enumerate(s):
    if element in set(t):
        list1.append(index)

if len(list1) > len(t):
    start   = list1[0]
    end     = list1[-1]


if s == t:
    ans = s
elif len(s) < len(t):
    ans = ''
elif len(s) == len(t) and set(s) != set(t):
    ans = ''

try:
    a = 1000
    for _ in range(len(s)*1000):
        ran_list    = random.choices(list1, k = 2)
        ran_list.sort()    
        if ran_list[1] - ran_list[0] > 200:
            continue
        new_start   = ran_list[0]
        new_end     = ran_list[1] + 1
        s_sub       = s[new_start:new_end]
        if s_in_t(s=s_sub, t=t):
            if new_end - new_start < a:
                a               = new_end - new_start
                start_we_want   = new_start
                end_we_want     = new_end - 1
except:
    pass

if a < 1000:
    ans = s[start_we_want:(end_we_want+1)]
elif s == t:
    ans = s
else:
    ans = ""

ans
# len("cmfuhcryjnpseriuwmfqzgfkqsjmfdmhrtbbwszhhozofhievpuuxzgntpzyvohmhkpffommfmamvlqtcmnaowphn")
true == ans