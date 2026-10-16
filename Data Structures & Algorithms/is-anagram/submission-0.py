#from collections import Counter
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        # Option 1^
        # Option 2:
        if len(s) != len(t):
            return False
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True

        # Option 3
        # if len(s) != len(t): return False

        # count = {}
        # for char in s:
        #     count[char] = count.get(char, 0) + 1
        
        # for char in t:
        #     if char not in count or count[char] == 0: # different check
        #         return False
        #     count[char] -= 1
        # return True
    
    # We can do this in three ways, we can use Counter, defaultdict, or hashmap
    # I like using defaultdict the most seeing as it is a better hashmap for frequency counters
    # In this problem you make sure the two lens are the same of the strings
    # We make a defaultdict which we always initialize with the type count = defaultdict(int)
    # Then we loop through one string and add to the count
    # Then we loop through the other string and subtract the count
    # We check, if count[char] < 0 then we return false since they should be all zero
    # Basically, check that the count[char] are equal to zero then we can return that it is true
    # We can also use a hashmap and just change the logic a bit but not by much
    # We can use the get method with hashmaps/dict
    # Just setting count to {}
    # Then count[char] = count.get(char, 0) + 1
    # ^^ This is basically the same as what default dict does automatically which is useful
    # Counter might not be allowed in an interview but it is still efficient C code in the background

    # One last thing is the difference in if checks in the end (last loop through the second string)
    # Is because the data structures react differently to accessing a missing key
    # Easier to work with defaultDict
    # if you do count[c] with dict and c does not exist it will raise a keyError
    # Checking for invalidity in defaultdict = count[char] < 0
    # Checking for invalidity in dict = 
    # if char not in count or count[char] == 0:

    # defaultdict silently initializes missing keys -  you detect too many of a character via negative counts
    # dict doesn't - you must check for existence before decrementing


        
        