class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0
        i = 0
        n = len(s)

        while i < n:
            if i + 1 < n:
                if (
                        (s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'))
                        or (s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'))
                        or (s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'))
                ):
                    ans += symbols[s[i + 1]] - symbols[s[i]]
                    i += 2
                    continue

            ans += symbols[s[i]]
            i += 1

        return ans

    # def romanToInt(self, s: str) -> int:
    #     symbols = {
    #         "I": 1,
    #         "V": 5,
    #         "X": 10,
    #         "L": 50,
    #         "C": 100,
    #         "D": 500,
    #         "M": 1000,
    #     }
    #
    #     total = symbols[s[len(s) - 1]]
    #
    #     for i in range(len(s) - 2, -1, -1):
    #         if symbols[s[i]] < symbols[s[i + 1]]:
    #             total -= symbols[s[i]]
    #         else:
    #             total += symbols[s[i]]
    #
    #     return total
    #
    # def romanToInt(self, s: str) -> int:
    #     symbols = {
    #         "I": 1,
    #         "V": 5,
    #         "X": 10,
    #         "L": 50,
    #         "C": 100,
    #         "D": 500,
    #         "M": 1000,
    #     }
    #
    #     ans = 0
    #     n = len(s)
    #     i = 0
    #
    #     while i < n:
    #         if i + 1 < n:
    #             if (
    #                 (s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"))
    #                 or (s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"))
    #                 or (s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"))
    #             ):
    #                 ans += symbols[s[i + 1]] - symbols[s[i]]
    #                 i += 2
    #                 continue
    #         ans += symbols[s[i]]
    #         i += 1
    #
    #     return ans
