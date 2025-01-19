class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            a = i*i
            b = (i+1)*(i+1)
            if a<= x < b:
                return i 
            i+=1

round()
        

print(Solution().mySqrt(1024))