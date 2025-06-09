class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def helper() -> str:
            nonlocal i
            ans = []
            k = 0
            while i < len(s):
                c = s[i]
                i += 1
                if c.isdigit():
                    k = 10 * k + int(c)
                elif c == '[':
                    ans.append(k * helper())
                    k = 0
                elif c == ']':
                    return ''.join(ans)
                else:
                    ans.append(c)

            return ''.join(ans)

        return helper()


# class Solution:
#     def decodeString(self, s: str) -> str:
#         count_stack = []
#         string_stack = []
#         curr_s = []
#         k = 0

#         for c in s:
#             if c.isdigit():
#                 k = k * 10 + int(c)
#             elif c == '[':
#                 count_stack.append(k)
#                 string_stack.append(''.join(curr_s))
#                 k = 0
#                 curr_s = []
#             elif c == ']':
#                 decoded_s = []
#                 decoded_s.append(string_stack.pop())
#                 decoded_s.extend(count_stack.pop() * curr_s)
#                 decoded_s = ''.join(decoded_s)
#                 curr_s = [decoded_s]
#             else:
#                 curr_s.append(c)

#         return ''.join(curr_s)


# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []

#         for c in s:
#             if c != ']':
#                 stack.append(c)
#             else:
#                 partial = []
#                 while stack[-1] != '[':
#                     partial.append(stack.pop())
#                 stack.pop()
#                 mul = []
#                 while stack and stack[-1].isdigit():
#                     mul.append(stack.pop())
#                 stack.extend(partial[::-1] * int(''.join(mul[::-1])))

#         return ''.join(stack)
