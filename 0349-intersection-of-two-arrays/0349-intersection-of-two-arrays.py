class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        n1=len(nums1)
        n2=len(nums2)
        # print(list(s))
        if n1>=n2:
            for i in nums1:
                if i in nums2 and i not in s:
                    s.append(i)
        else:
            for i in nums2:
                if i in nums1 and i not in s:
                    s.append(i)
        return s

        