class Solution:
    def trap(self, height: List[int]) -> int:
        # ans=0
        # r_max=0
        # l_max=0
        # i=0
        # j=len(height)-1
        # while i<j:
        #     l_max=max(l_max,height[i])
        #     r_max=max(r_max,height[j])
        #     if l_max<r_max:
        #         ans+=(l_max-height[i])
        #         i+=1
        #     else:
        #         ans+=(r_max-height[j])
        #         j-=1
        # return ans

        r_max=[0]*len(height)
        l_max=[0]*len(height)
        l_max[0]=height[0]
        for i in range(1,len(height)):
            l_max[i]=max(l_max[i-1],height[i])

        r_max[len(height)-1]=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            r_max[i]=max(r_max[i+1],height[i])
        ans=0
        for i in range(len(height)):
            a=min(l_max[i],r_max[i])
            ans+=(a-height[i])
        return ans

