class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            date1, date2 = date2, date1

        past_d = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8:212, 9: 243, 10: 273, 11: 304, 12: 334}
        def number_of_days(date: str) -> int:
            count = 0
            year, month, day = map(int, date.split(sep='-'))

            count += (year - 1971) * 365 + past_d[month] + day - 1
            # Count for leap years.
            if year >= 1972:
                count += 1 + (year - 1972) // 4
            if year >= 2000:
                count -= 1 + (year - 2000) // 100
            if year >= 2000:
                count += 1 + (year - 2000) // 400
            if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month < 3:
                count -= 1
            return count

        return number_of_days(date2) - number_of_days(date1)
