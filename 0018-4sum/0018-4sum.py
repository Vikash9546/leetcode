class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        i=0
        while i<n:
            j=i+1
            while j<n:
                goal=target-nums[i]-nums[j]
                left=j+1
                right = n-1
                while left<right:
                    s=nums[left]+nums[right]
                    if s==goal:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left+1 < n and nums[left+1] == nums[left]:
                            left += 1
                        
                        left+=1
                        right-=1
                        
                    elif s<goal:
                        left+=1
                    else:
                        right-=1
                while j+1 < n and nums[j+1] == nums[j]: j += 1 
                j += 1
                        
            while i+1 < n and nums[i+1] == nums[i]: i += 1 
            i += 1
        return res



        