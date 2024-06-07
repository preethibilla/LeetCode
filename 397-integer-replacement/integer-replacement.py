class Solution:
    def integerReplacement(self, n: int) -> int:
        if(n==1):
            return 0
        
        if(n%2==0):
            return 1 + self.integerReplacement(n//2)
        else:
            return min(1 + self.integerReplacement(n+1),1 + self.integerReplacement(n-1))
        
            
        