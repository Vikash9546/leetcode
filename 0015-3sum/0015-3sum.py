class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def helper(i,nums,d):
            k=i+1
            j=len(nums)-1
            while k<j:
                s=nums[i]+nums[k]+nums[j]
                if s==0:
                    d.append([nums[i],nums[k],nums[j]])
                    k+=1
                    j-=1
                    while (k<j) and nums[k]==nums[k-1]:
                        k+=1
                    while (k<j) and nums[j]==nums[j+1]:
                        j-=1

                elif s>0:
                    j-=1
                else:
                    k+=1
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i==0 or nums[i-1]!=nums[i]:
                helper(i,nums,res)
        return res

            
                    
        