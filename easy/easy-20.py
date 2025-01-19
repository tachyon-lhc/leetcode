class Solution:
    def isValid(self, s: str) -> bool:
   arr = [] 
    for c in s:
      if c in '({[':
        arr.append(c)
    else:
        if not arr:
            return False
        if c == ')' and arr[-1] != '(':
            return False
        if c == '}' and arr[-1] != '{':
            return False
        if c == ']' and arr[-1] != '[':
            return False
        arr.pop()

print(isValid("()"))  # True
