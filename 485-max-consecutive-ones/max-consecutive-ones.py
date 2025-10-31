class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcon = 0
        count=0
        pt2=0

        while(pt2 < len(nums)):
            if nums[pt2] == 1:
                pt2 = pt2+1
                count = count+1
            elif nums[pt2] == 0:  
                count = 0
                pt2=pt2+1
            maxcon = max(count,maxcon)
        return maxcon


            

            
