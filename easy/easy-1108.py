class Solution:
    def defangIPaddr(self, address: str) -> str:
        clean_address = address.split('.')
        return '[.]'.join(clean_address)
    
print(Solution().defangIPaddr("1.1.1.1"))