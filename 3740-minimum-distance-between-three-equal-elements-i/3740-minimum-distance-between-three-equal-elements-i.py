class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        index_m = {}

        for i in range(len(nums)):
            if nums[i] in index_m:
                index_m[nums[i]].append(i)
            else:
                index_m[nums[i]] = [i]

        m_p = float('inf')

        for key in index_m:
            arr = index_m[key]

            if len(arr) >= 3:
                for i in range(len(arr) - 2):
                    a = 2 * (arr[i + 2] - arr[i])
                    if a < m_p:
                        m_p = a

        return -1 if m_p == float('inf') else m_p