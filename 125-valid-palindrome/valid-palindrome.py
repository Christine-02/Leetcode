class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = "".join(word.lower() for word in s if word.isalnum())
        return newstr == newstr[::-1]