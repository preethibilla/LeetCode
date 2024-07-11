class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Initialize an empty stack to simulate the operations
        stack = []
        
        # Index for the popped array
        j = 0
        
        # Iterate through each number in the pushed array
        for num in pushed:
            # Push the current number onto the stack
            stack.append(num)
            
            # While the stack is not empty and the top of the stack equals the next number to pop
            while stack and stack[-1] == popped[j]:
                # Pop the number from the stack
                stack.pop()
                # Move to the next number in the popped sequence
                j += 1
        
        # If the stack is empty, all elements have been popped in the correct order
        return not stack
        