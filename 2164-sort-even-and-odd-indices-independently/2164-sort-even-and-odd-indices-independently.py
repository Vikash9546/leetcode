class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        f=0
        s=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even[f]
                f+=1
            else:
                nums[i]=odd[s]
                s+=1
        return nums

                
            


        

        