class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = []
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append(current_num)
                stack.append(current_str)
                current_num = 0
                current_str = []
            elif char == ']':
                prev_str = stack.pop()
                repeat_times = stack.pop()
                current_str = prev_str + current_str * repeat_times
            else:
                current_str.append(char)
        
        return ''.join(current_str)
        