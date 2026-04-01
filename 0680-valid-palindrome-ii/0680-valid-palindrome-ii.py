class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        def helper(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        while i<j:
            if s[i]!=s[j]:
                return helper(i+1,j) or helper(i,j-1)
            else:
                i+=1
                j-=1
        return True

        