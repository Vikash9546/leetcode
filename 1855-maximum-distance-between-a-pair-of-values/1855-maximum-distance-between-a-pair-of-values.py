class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        max_v=float('-inf')
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                if i<=j:
                    max_v=max(abs(j-i),max_v)
                else:
                    j+=1
                j+=1
            else:
                i+=1
        if max_v==float('-inf'):
            return 0
        return max_v



        