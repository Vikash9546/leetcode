class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # s=[]
        # n1=len(nums1)
        # n2=len(nums2)
        # # print(list(s))
        # if n1>=n2:
        #     for i in nums1:
        #         if i in nums2 and i not in s:
        #             s.append(i)
        # else:
        #     for i in nums2:
        #         if i in nums1 and i not in s:
        #             s.append(i)
        # return s

        nums1.sort()
        nums2.sort()
        res=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                if nums1[i] not in res:
                    res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return res

        