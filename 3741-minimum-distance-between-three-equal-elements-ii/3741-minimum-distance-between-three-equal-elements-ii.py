class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums)<2:
            return -1
        index_m={}
        for i in range(len(nums)):
            if nums[i] in index_m:
                index_m[nums[i]].append(i)
            else:
                index_m[nums[i]]=[i]
        # print(index_m)
        m_p=float('inf')
        for key in index_m:
            arr=index_m[key]
            for i in range(len(arr)-2):
                m_p=min(m_p,2*(arr[i+2]-arr[i]))
        if m_p == float('inf'):
            return -1
        return m_p
        
        
        