class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        v=heights.copy()
        # print(c)
        heights.sort()
        c=0
        for i in range(len(heights)):
            if v[i]!=heights[i]:
                c+=1
        return c

        