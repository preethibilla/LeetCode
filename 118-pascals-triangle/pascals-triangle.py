class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Set the basecase, [1] in results
        results = [[1]]

        # Generate number of rows as requested
        for i in range(1, numRows):
            # Add zeros to the beginning and end of previous row for calculation
            row = [0] + results[-1] + [0]

            # For each item in row, set it to be itself plus the next number
            for j in range(len(row) - 1):
                row[j] = row[j] + row[j + 1]

            # Remove the last zero, because we only need one new number
            row.pop()
            # Append the new row to results
            results.append(row)
        
        # Return the results
        return results
        