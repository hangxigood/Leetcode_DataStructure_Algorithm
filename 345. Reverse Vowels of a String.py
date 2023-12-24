# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        pointer = []
        vowels = ['a', 'A', 'E', 'e', 'I', 'i', 'o', 'O', 'u', 'U']
        s = list(s)
        for index,x in list(enumerate(s)):
            if x in vowels:
                pointer.append(index)
        for n in range(len(pointer)//2):
            middle = s[pointer[-n-1]]
            s[pointer[-n-1]] = s[pointer[n]]
            s[pointer[n]] = middle
        return ''.join(s)
