class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        e=0
        for i in nums:
            while i>0:
                e+= i%10
                i=i//10


        return abs(s-e)
        