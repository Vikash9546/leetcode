class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        m_v=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                m_v=min(m_v,abs(i-start))
        return m_v


        