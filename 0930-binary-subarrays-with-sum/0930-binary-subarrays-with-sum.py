class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # prefix=[0]*len(nums)
        # prefix[0]=nums[0]
        # for i in range(1,len(nums)):
        #     prefix[i]=prefix[i-1]+nums[i]
        # c=0
        # for i in range(len(nums)):
        #     start=i
        #     end=len(nums)-1
        #     while start<=end:
        #         mid=(start+end)//2
        #         if goal+nums[i]==prefix[mid]:
        #             c+=1
        #         elif goal+nums[i]>prefix[mid]:
        #             start=mid+1
        #         else:
        #             end=mid-1
        # return c

        curr_s=0
        d={0:1}
        c=0
        for i in nums:
            curr_s+=i
            if (curr_s-goal) in d:
                c+=d[curr_s-goal]
            if curr_s in d:
                d[curr_s]+=1
            else:
                d[curr_s]=1
                
        return c

    