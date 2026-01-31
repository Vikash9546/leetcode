class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        dist = math.inf
        nums.sort()
        
        for i in range(len(nums)):
            if 3*nums[i]-target >= dist:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j = i+1
            k = len(nums)-1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
            
                if total > target:
                    k -= 1
                    if total-target < dist:
                        res = total
                        dist = total-target
                elif total < target:
                    j += 1
                    if target-total < dist:
                        res = total
                        dist = target-total

                    while j < len(nums) and nums[j-1]==nums[j]:
                        j += 1
                else:
                    return target
        return res