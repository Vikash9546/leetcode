class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        v=s.split(" ")
        # print(v)
        return len(v[-1])
        