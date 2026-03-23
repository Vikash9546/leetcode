class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        e=0
        for i in nums:
            j=str(i)
            for k in j:
                e+=int(k)

        return abs(s-e)
        