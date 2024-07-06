class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Find the frequency of the most common task
        max_freq = max(task_counts.values())
        
        # Find how many tasks have this maximum frequency
        max_freq_count = list(task_counts.values()).count(max_freq)
        
        # Calculate the minimum length of intervals needed
        # (max_freq - 1) represents the number of full cycles of `n` intervals
        # `max_freq_count` is the number of tasks with the maximum frequency
        min_intervals = (max_freq - 1) * (n + 1) + max_freq_count
        
        # The result is the maximum of either the calculated minimum intervals
        # or the total number of tasks (if there are more tasks than idle slots)
        return max(min_intervals, len(tasks))
        