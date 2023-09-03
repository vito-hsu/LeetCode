dictionary = ["cat","bat","rat"] ; sentence = "the cattle was rattled by the battery"       # Output: "the cat was rat by the bat"
dictionary = ["a","b","c"] ; sentence = "aadsfasf absbs bbab cadsfafs"                      # Output: "a a b c"




class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        key_list = sentence.split(" ")
        key_set = set(dictionary)

        for ind, ele in enumerate(key_list):
            st = ""
            for r in ele:
                st += r
                if st in key_set:
                    key_list[ind] = st
                    break
        
        return " ".join(key_list)


