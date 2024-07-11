class Solution:
    def calculate(self, s: str) -> int:
        # Stack to hold intermediate results and signs
        stack = []
        current_number = 0
        current_result = 0
        current_sign = 1  # 1 for positive, -1 for negative
        
        for char in s:
            if char.isdigit():
                # Build the current number
                current_number = current_number * 10 + int(char)
            elif char == '+':
                # Apply the current number with its sign to the result
                current_result += current_sign * current_number
                # Set the current sign to positive
                current_sign = 1
                # Reset the current number
                current_number = 0
            elif char == '-':
                # Apply the current number with its sign to the result
                current_result += current_sign * current_number
                # Set the current sign to negative
                current_sign = -1
                # Reset the current number
                current_number = 0
            elif char == '(':
                # Push the current result and sign onto the stack
                stack.append(current_result)
                stack.append(current_sign)
                # Reset the result and sign for the new sub-expression
                current_result = 0
                current_sign = 1
            elif char == ')':
                # Apply the current number with its sign to the result
                current_result += current_sign * current_number
                # Pop the sign before the parenthesis and apply it to the current result
                current_result *= stack.pop()
                # Pop the result calculated before the parenthesis and add it to the current result
                current_result += stack.pop()
                # Reset the current number
                current_number = 0
        
        # Add any remaining number to the result
        return current_result + (current_sign * current_number)



        