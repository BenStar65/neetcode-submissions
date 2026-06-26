class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_word = s.replace(" ", "")
        new_s = ""
        punctuation = "!@#$%^&*()_+-=.,;'\":[]\\{\\}\\?<>/"
        palindrome = ""

        for i in range(len(strip_word)):
            if strip_word[i] in punctuation:
                 continue
            else:
                 new_s += strip_word[i]
        
        
        for i in range(len(new_s) - 1, - 1, - 1):
              palindrome += new_s[i]
           
        if new_s.lower() == palindrome.lower():
              return True
        else:
              return False


        