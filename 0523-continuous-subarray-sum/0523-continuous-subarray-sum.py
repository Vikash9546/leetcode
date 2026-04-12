class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_map = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            rem = prefix_sum % k

            if rem in remainder_map:
                if i - remainder_map[rem] >= 2:
                    return True
            else:
                remainder_map[rem] = i

        return False