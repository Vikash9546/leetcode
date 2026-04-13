class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map={}
        for i in range(len(arr1)):
            if arr1[i] in map:
                map[arr1[i]].append(i)
            else:
                map[arr1[i]]=[i]
        # print(map)
        res=[]
        for i in arr2:
            for j in map[i]:
                res.append(arr1[j])
        arr1.sort()       
        for i in arr1:
            if i not in arr2:
                res.append(i)
        return res
        
        