class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        a=0
        for i in sentences:
            a=max(len(i.split(" ")),a)
            # a=max(len(i.split(' ')))
        return a
        