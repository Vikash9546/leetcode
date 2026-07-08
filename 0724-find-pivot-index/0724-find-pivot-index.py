class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_t = 0
        right_t = 0
        for i in range(len(nums)):
            if i!=0:
                left_t+=nums[i-1]    
            right_t = s - left_t - nums[i]
            if left_t==right_t:
                return i
        return -1




        