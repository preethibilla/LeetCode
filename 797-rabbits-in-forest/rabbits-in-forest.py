class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        count = 0

        for answer in answers:
            if answer == 0:
                # This must be the only rabbit of its color.
                count += 1
            elif answer not in freq or freq[answer] == 0:
                # This is the first time the color appears.
                freq[answer] = 1
                # Add all rabbits having this new color.
                count += answer + 1
            else:
                # Add one to how many times answer occurred.
                freq[answer] += 1
                if freq[answer] > answer:
                    # If n+1 rabbits have said n,
                    # this color group is complete.
                    freq[answer] = 0
        
        return count

        