class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""
        for ch in s:

            if ch.isalnum():
                cleaned = cleaned + ch.lower()

        reversed_string = ""
        for i in range(len(cleaned) - 1, -1, -1):

            reversed_string = reversed_string + cleaned[i]

        if cleaned == reversed_string:
            return True
        else:
            return False