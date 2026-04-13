class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        e=''
        for i in range(len(s)):
            e+=s[(i+k)%len(s)]
        return e
        