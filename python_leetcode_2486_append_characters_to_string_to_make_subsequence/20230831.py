s = "coaching" ; t = "coding"           # Output: 4
s = "abcde" ; t = "a"                   # Output: 0
s = "z" ; t = "abcde"                   # Output: 5
s = "dj" ; t = "xnb"                    # 3
s = "kmeqwbmaymnouefjdkqdzkgznooulizyerzqrelyrdlgvvtywugwhsvuhqwwzrogsxdtdbjlqqhmbnwvrdxfvavfjkawvxxbsavymfjplbafoljfilxumdxkauhithnuryedfseqdzwqdtfpfhnhzriivjlvcuwxpcrkalvkrvkxvcouxwhawmjjdnmhctfkwxhoxjggplgcstjnuxhfhaoniqcfvkekzjcycjjdkbefxkzejzhsdgnttecmrmddpllqijvqfrlczvwtvrnlslfnesatavkdocvtgqhjjkiiwzyigzfobvmjjudvhhtusvqhpysmbcyypmiazjttkljbhzyfbwonwrqrunaamqsahvfihwnxjffipwbihutdaezfsoztrqctloljvvevvdyrkmkyubjdgtvbowjiswdrivrbxatkkcxirvhkzrfmuwbslzcjincffnanjbovxahubcnravizpibdeansgxsbjjdyvnuqzlsznjvaezehegyvosoatfnnqvpqhpxthrnqgkgchjxkdmlpygxpgmcorchqveyxjogzryhvcozqkasumkaaevscaetpxhewwoewmizvaoulpuefmoishuifkvqxrxuebwclzzm"
t = "dhjexhsvmnlifeeibuirosaaoxcnipishzcvzpixjfrjxhyzepigqktjashiszxdpdbyeqhcjcthogczowbmbtqxwvtbpxbpqgxzwlbwvzzvbknlgytaerzfzxumfondridapbwodizbmitrlriclhvnwwsrkdyjhzqtckfgpciqghxoeuuybuivqhvwdwricrppltbfhraiwticbvrlncooksgeuqatttysuuwqbuivekxcdbtlxyxplhobrsspcfalcwvbbcavljocxbwwpnncrswxqbkhioywrknmthcsxxldyembvkibjdgbsoyrfnmeccwxbvsstekwciclgbiplgfbvbgasntgofipcvhspoieyytruyuyauroyjdjoeqshubpyoaigzochuyroepjpzduwhudmnkewphjwkpgevyaxcgwbsdlvzwvkcmzblibddtjcgbkmpkwefthqkuiqptdqkpnuwrbwwpuxlombjufdowbqixooenjkvnslhhpjnmikmqsgobnsimhszzrsrdmuvbjdiixvzzlcdmevhdajybnxhvtbbasgpvqangnhkcfutlsndfylikjmktzmdcypchehhwusrvvsldqfygwwcoleueklokqqrelqylubfggguivqyvlpvafjstltzhsdaedxpsjxuzuohaftfcwsdcvqoqlrtkpavaskiiuvqkhfzatbfrwajlqxoaysqygcgrkzchhdzugqtqlugzmbimxejyspaoqzrebbzobbvppvlajbgrakbnxlafptwazozvvmsxosvlzreuibwanuknjocbkpepctlfnqriypdcyppmlxavbvyvqnomczqqzsnkjncyqnalytbytsujqwvfaxwksqnooarrjkrgferrmhhnggmumzlpnozjlktrwtusqphumkpltgwszsjwgsvxjqsefr"
s = "a" ; t = "z"                       # 1

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        for ind1, t_ele in enumerate(t):                        # ind1 = 0 ; t_ele = t[0]
            if len(s)==0:
                break
            for ind2, s_ele in enumerate(s):
                # print(t_ele, s_ele)
                if s_ele == t_ele:
                    s = s[ind2+1:]
                    break
            if s_ele == t_ele:
                continue
            else:
                break        
        if ind1==len(t)-1 and s_ele != t_ele:
            return 1
        elif ind1==len(t)-1 and s_ele == t_ele:
            return 0
        return len(t[ind1:])