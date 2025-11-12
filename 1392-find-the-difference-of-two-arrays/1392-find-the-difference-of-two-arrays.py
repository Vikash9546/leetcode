class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[0]*2
        a=[]
        b=[]
        for i in nums1:
            if  i in nums2:
                continue
            if i in a:
                continue
            a.append(i)
        for i in nums2:
            if  i in nums1:
                continue
            if i in b:
                continue
            b.append(i)
        answer[0]=a
        answer[1]=b
        return answer




        