class Solution:
    def integerReplacement(self, n: int) -> int:
        # if(n==1):
        #     return 0
        
        # if(n%2==0):
        #     return 1 + self.integerReplacement(n//2)
        # else:
        #     return min(1 + self.integerReplacement(n+1),1 + self.integerReplacement(n-1))
        visited = dict()
        return self.getIntegerReplacement(visited, n)
    def getIntegerReplacement(self, visited, n):
        if(n==1):
            return 0
        
        if(n in visited):
            return visited[n]
        
        if(n%2==0):
            result = 1 + self.getIntegerReplacement(visited, n//2)
        else:
            result = min(1 + self.getIntegerReplacement(visited, n+1),1 + self.getIntegerReplacement(visited, n-1))
        visited[n] = result
        return result
        

        
            
        