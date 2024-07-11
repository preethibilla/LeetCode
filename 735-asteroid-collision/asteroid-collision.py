class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Initialize an empty stack to keep track of asteroids still moving
        stack = []
        
        # Iterate through each asteroid in the input list
        for asteroid in asteroids:
            # Determine if the current asteroid needs to be pushed to the stack
            push = True
            
            # Handle collisions for asteroids moving to the left
            while stack and asteroid < 0 < stack[-1]:
                # Compare sizes of the colliding asteroids
                if stack[-1] < -asteroid:
                    # The right-moving asteroid is smaller and explodes
                    stack.pop()
                elif stack[-1] == -asteroid:
                    # Both asteroids are the same size and explode
                    stack.pop()
                    push = False
                    break
                else:
                    # The right-moving asteroid is larger, the left-moving asteroid explodes
                    push = False
                    break
            
            # If the current asteroid is not destroyed, push it to the stack
            if push:
                stack.append(asteroid)
        
        # Return the state of the asteroids after all collisions
        return stack
        