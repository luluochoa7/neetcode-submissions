class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
    
    
    def alphaNum(self, char):
        return (
            ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )


# For a valid palindrome, if we want to check for A-Z, a-z, and 0-9 we have to create a
# separate function named alphaNum where we check whether the char in question is in the
# range. This allows for 0(1) space which is the best solution.
# We have this function then we go through the two pointer solution
# Creating left and right and creating a while loop as usual
# Within this while loop we have this structure
# while loop for left
# while loop for right
# if statement to check if not equal: return False
# Change pointers for both left and right
# The one thing to remember is that in the inner while loops since we are continually
# moving left and right we have to ensure two things
# 1. left < right or right > left
# 2. and not self.alphaNum(s[right]) or not self.alphaNum(s[left])
# We check not for self.alphaNum because we only want to move the pointer when the char
# in question is not alphaNumber so not true
# This is ensuring we do not pass the two pointers within the inner while loops

# Biggest thing to remember is that when we have to create a separate function to
# get the better space complexity but the helper function is really easy to write
# Just use ord('A') ord(0) and <= <= signs with the char in the middle

        