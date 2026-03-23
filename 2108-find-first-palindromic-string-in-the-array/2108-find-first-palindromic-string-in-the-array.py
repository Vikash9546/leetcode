class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def call(i):
            j=0
            k=len(i)-1
            while j<k:
                if i[j]!=i[k]:
                    return False
                
                j+=1
                k-=1
            return True

        for i in words:
            if call(i):
                return i
        return ''
            


        