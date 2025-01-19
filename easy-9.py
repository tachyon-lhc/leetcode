class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reverseNum = num[::-1]

        return(num == reverseNum)

print(Solution().isPalindrome(11))

