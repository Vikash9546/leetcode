class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        for i in range(n):
            result.append(nums[(i+nums[i])%n])
        
        return result
            



        