class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Optimization #1: sort to break early
        result = []

        def backtrack(start: int, path: List[int], target_left: int):
            if target_left == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target_left:
                    break  # No point in exploring further
                path.append(candidates[i])
                backtrack(i, path, target_left - candidates[i])  # Reuse same i
                path.pop()

        backtrack(0, [], target)
        return result

        