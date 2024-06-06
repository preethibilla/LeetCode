class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        n = len(s)
        sum = 0
        for i in range(n):
            if i < n-1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                sum -= roman_to_int[s[i]]
            else:
                sum += roman_to_int[s[i]]
        return sum

        