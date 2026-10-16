class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False


        # Here what I do is use a set by calling numSet = set()
        # Then I loop through nums
        # I check if num is in numSet by using if num in numSet (can do this with sets aka check for matches)
        # Then I return True (capital) if so
        # If not then I just add num to numSet by calling .add()
        # Finally outside the loop I return False (capital)