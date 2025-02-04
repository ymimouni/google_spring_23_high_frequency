from random import choice
from typing import List


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match_count(s: str, t: str) -> int:
            """
            Calculate the number of exact matches.
            """
            return sum(1 for c, d in zip(s, t) if c == d)

        candidates = words[:]
        for _ in range(30):
            candidate = choice(candidates)
            match = master.guess(candidate)
            if match == 6:
                return None

            candidates = [word for word in candidates if match_count(word, candidate) == match]

        return None
