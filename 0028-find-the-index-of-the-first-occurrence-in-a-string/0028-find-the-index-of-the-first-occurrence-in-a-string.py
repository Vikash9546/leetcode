class Solution:
    def strStr(self, haystack, needle):
        n=len(needle)
        m=len(haystack)
        j=0
        s=haystack[j:n]
        i=n
        
        while i-1<m:
            if s==needle:
                return j
            else:
                j+=1
                i+=1
                s=haystack[j:i]
        return -1

       