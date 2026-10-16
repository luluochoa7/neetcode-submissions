class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxNumber = float("-inf")
        currentMaxNumber = 0

        for num in nums:
            if num == 1:
                currentMaxNumber += 1
            else:
                currentMaxNumber = 0

            maxNumber = max(maxNumber, currentMaxNumber)

        return maxNumber
            
        