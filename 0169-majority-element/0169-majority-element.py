class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1

        for i,j in d.items():
            if j == max(d.values()):
                return i  

        