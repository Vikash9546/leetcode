class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        total_gas=0
        real_t_g=0
        start_idx = 0
        for i in range(n):
            diff = gas[i]-cost[i]
            total_gas+=diff
            real_t_g+=diff
            if real_t_g<0:
                real_t_g=0
                start_idx=i+1
        if total_gas>=0:
            return start_idx
        else:
            return -1
        