class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = defaultdict(int)
        sum_rabbits = 0

        for answer in answers:
            if answer == 0:
                sum_rabbits += 1
            elif counts[answer] == 0:
                counts[answer] = 1
                sum_rabbits += answer + 1
            elif counts[answer] < answer + 1:
                counts[answer] += 1
            else:
                counts[answer] = 1
                sum_rabbits += answer + 1

        return sum_rabbits

        