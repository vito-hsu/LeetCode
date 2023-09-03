columnNumber = 1        # Output: "A"
columnNumber = 10       # Output: "J"
columnNumber = 26       # Output: "Z"       26//26=1
columnNumber = 52       # Output: "AZ"      52//26=2(B)     52%26=0
columnNumber = 28       # Output: "AB"      28//26=1(A)     28%26=2(B)
columnNumber = 701      # Output: "ZY"      701//26=26(Z)   701%26=25(Y)
columnNumber = 702      # Output: "ZZ"      702//26=27      702%26=0
columnNumber = 703      # Output: "AAA"     702//26=27      703%26=1
columnNumber = 7010     # Output: "JIP"     7010//26=269    269//26=10(J)   7010%(26*26)=250    250//26=9(I)    250%26=16(P)
columnNumber = 280000   # Output: "OXEF"



class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        hash_table = {
            '1':'A',  '2':'B',  '3':'C',  '4':'D',  '5':'E',  '6':'F',  '7':'G',  '8':'H',  '9':'I',  '10':'J', 
            '11':'K', '12':'L', '13':'M', '14':'N', '15':'O', '16':'P', '17':'Q', '18':'R', '19':'S', '20':'T',           
            '21':'U', '22':'V', '23':'W', '24':'X', '25':'Y', '26':'Z' 
        }
        ans = ''
        original = True

        if columnNumber%26==0:
            original = False
            columnNumber = columnNumber-1

        while True and columnNumber!=0:
            key_value = 26
            while columnNumber//key_value>26:
                key_value *= 26

            if columnNumber>26:
                ans = ans + hash_table[str(columnNumber//key_value)] 

            if columnNumber%key_value<=26:
                ans = ans + hash_table[str(columnNumber%key_value)]
                break

            columnNumber = columnNumber%key_value


        if original == False:
            i = -1
            ans = list(ans)
            # while True:
            #     if ans[i]!='Z':
            new_string = hash_table[str(int(next(key for key, value in hash_table.items() if value == ans[i]))+1)]
            ans[i] = new_string
                    # break
                # else:
                #     new_string = 'A'
                #     ans[i] = new_string
                #     i -= 1
            ans = ''.join(ans)

        return ans