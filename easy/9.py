class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if "-" in x:
            return False # -negatives are not palindromes
        if x[::-1] == x: # string slicing to flip string
            return True  
        else:
            return False   
    
result = Solution()
print(result.isPalindrome(22))