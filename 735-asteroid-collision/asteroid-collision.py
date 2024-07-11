class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
		# determine which asteroids are exploding
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
		    # considered asteroid might still destroy others so continue checking
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
	    # if nothing on the stack, 
            else:
                stack.append(asteroid)
        return stack
        