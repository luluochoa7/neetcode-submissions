class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # One Pass Solution
        numIndex = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in numIndex:
                return [numIndex[difference], i] # here I need to remember to return the lower one first which would be what is in the hashmap
            numIndex[num] = i

        # Two Pass Solution
        # numIndex = {}
        # for i, num in enumerate(nums):
        #     numIndex(num) = i


        # for i, num in enumerate(nums):
        #     difference = target - num
        #     if difference in numIndex and numIndex[difference] != i: # for this two pass solution I need to make sure the two indices I am about to return are not equal
        #         return [i, numIndex[difference]]
        #     numIndex[num] = i
        

        
            

        # We build out a hashmap. We can do this in one pass or two.
        # We can create a hashmap by just using {}
        # prevMap = {}
        # indices = {}
        # to set something we use
        # indices[n] = i so we get (num, i) pairs
        # we use target - nums[i] as well to see if we found the pair
        # We can return the indices so one will be the current index in our enumeration and also the hashmap instance of that so we do indices[num] to get the index
        # We can combine them by just putting them in a bracket which indicates a array



        
            

        



        