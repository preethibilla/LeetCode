class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Add a zero height bar to the end to ensure all bars are processed
        stack = [-1]  # Initialize stack with -1 to handle empty stack scenarios gracefully
        maxArea = 0  # Variable to store the maximum area found

        for i in range(len(heights)):  # Iterate through all bars in the histogram
            # While the current bar is less than the bar at the index stored at the top of the stack
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]  # Get the height of the bar
                width = i - stack[-1] - 1  # Calculate the width of the rectangle
                maxArea = max(maxArea, height * width)  # Update the maximum area found

            stack.append(i)  # Add the current index to the stack

        heights.pop()  # Remove the zero height bar added at the beginning
        return maxArea  # Return the maximum area found
        