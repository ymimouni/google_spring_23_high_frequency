class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n:
            return "0"

        stack = []
        for digit in num:
            while k and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)

        stack = stack[:-k] if k else stack

        return ''.join(stack).lstrip("0") or "0"
