class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        w = word.upper()
        s=set()
        for i in w:
            s.add(i)
        count= 0
        lst = list(s)
        for i in lst:
            if i in word and i.lower() in word:
                count+=1
        return count


        