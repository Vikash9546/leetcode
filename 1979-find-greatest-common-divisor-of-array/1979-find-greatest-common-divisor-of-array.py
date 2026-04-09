class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math
        mi=min(nums)
        ma=max(nums)
        return math.gcd(mi,ma)
        