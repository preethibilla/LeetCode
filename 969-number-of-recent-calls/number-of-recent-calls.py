class RecentCounter:

    def __init__(self):
        # Creation of new queue to store timestamops of calls
        self.queue = deque()
        
    def ping(self, t: int) -> int:
        # Upon ping, add the current timestamp to queue
        self.queue.append(t)
        # remove timestamps that are outside the 3000 milliseconds window
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        #length of the queue represents the number of calls within the window
        return len(self.queue)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)