class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_s=float('inf')
        curr_s=0
        i=j=0
        while i<len(nums) and j<len(nums):
            curr_s+=nums[j]
            while curr_s>=target:
                curr_s-=nums[i]
                min_s=min(min_s,(j-i)+1)
                i+=1
            j+=1
        if min_s == float('inf'):
            return 0
        return min_s
        