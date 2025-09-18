#https://leetcode.com/problems/palindrome-number/submissions/1774745259

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_str = str(x)        
        return x_str == x_str[::-1]