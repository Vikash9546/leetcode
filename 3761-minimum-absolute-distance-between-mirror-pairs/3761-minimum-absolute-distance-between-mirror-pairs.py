class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        res = float('inf')
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                res = min(res, i - seen[n])
            seen[int(str(n)[::-1])] = i
        if res==float('inf'):
            return -1
        else:
            return res