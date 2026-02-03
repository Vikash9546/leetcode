class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n=1
        lis=[1]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                n=max(n,n+1)
                
            else:
                lis.append(n)
                n=1
        lis.append(n)
        return max(lis)
        