# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)

        if len_s == 1:
            return False

        for i in range(1, len_s//2+1):
            for j in range(1, len_s//i+1):
                if s[0:i]*j==s:
                    return True
        return False
