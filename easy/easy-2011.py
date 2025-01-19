class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        solutions = {'++X':1, 'X++':1, '--X':-1, 'X--':-1}
        return sum(solutions[i] for i in operations)
 
print(Solution().finalValueAfterOperations(["++X","++X","X++"]))