# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

# Solution 1
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
 
        if str1 + str2 == str2 + str1:
            return str1[:math.gcd(len(str1), len(str2))]
        else:
            return ''

# Solution 2
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
 
        if len(str1) >= len(str2):
            shorter = str2
            longer = str1
        else:
            shorter = str1
            longer = str2

        max_times = len(longer) # if the large_str just has one character, the max_times = len(longer) / 1 

        for i in range(len(shorter),0,-1): # try the large_str from full shorter to the first character from shorter
            flag1 = False
            flag2 = False
            for j in range(1,max_times+1): # for one large_str, try different max_times
                if shorter[0:i] * j == str2:
                    flag1 = True
                if shorter[0:i] * j == str1:
                    flag2 = True

            if flag1 and flag2:
                return shorter[0:i]

        return ''
