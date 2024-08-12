class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        side_length = perimeter // 4
        sides = [0] * 4
        matchsticks.sort(reverse = True)
        def backtrack(index):
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side_length
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if backtrack(index+1):
                        return True
                    sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break
            return False
        return backtrack(0)
     
        