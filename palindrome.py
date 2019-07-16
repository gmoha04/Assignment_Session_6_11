class palindrome:
    def __init__(self,s):
        self.s=s
    def isPalindrome(self): 
        if (self.s == self.s[::-1]): 
            return True
        else:
            return False