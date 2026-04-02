class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        r_max=0
        l_max=0
        i=0
        j=len(height)-1
        while i<j:
            l_max=max(l_max,height[i])
            r_max=max(r_max,height[j])
            if l_max<r_max:
                ans+=(l_max-height[i])
                i+=1
            else:
                ans+=(r_max-height[j])
                j-=1
        return ans