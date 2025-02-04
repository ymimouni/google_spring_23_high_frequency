class Solution:
    def employeeFreeTime(self, schedules):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        from heapq import heappush, heappop

        def work_time_gen():
            q = []
            idx = [0] * len(schedules)

            for i, schedule in enumerate(schedules):
                heappush(q, (schedule[idx[i]].start, schedule[idx[i]].end, i))
                idx[i] += 1

            while q:
                s, e, i = heappop(q)
                if idx[i] < len(schedules[i]):
                    heappush(q, (schedules[i][idx[i]].start, schedules[i][idx[i]].end, i))
                    idx[i] += 1
                yield s, e

        free_times = []
        work_times = work_time_gen()
        prev_end = next(work_times)[1]

        for start, end in work_times:
            if start > prev_end:
                free_times.append(Interval(prev_end, start))
            prev_end = max(prev_end, end)

        return free_times


# from itertools import chain
#
#
# class Solution:
#     def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
#         sorted_sch = sorted(chain.from_iterable(schedule), key=lambda i: i.start)
#         free_time = []
#         curr = sorted_sch[0]
#         for next_ in sorted_sch[1:]:
#             if curr.end >= next_.start:
#                 curr = Interval(curr.start, max(curr.end, next_.end))
#             else:
#                 free_time.append(Interval(curr.end, next_.start))
#                 curr = next_
#
#         return free_time
#
#
# class Solution:
#     def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
#         def free_time(emp_schedule):
#             free_schedule = [Interval(float("-inf"), emp_schedule[0].start)]
#             for i in range(len(emp_schedule) - 1):
#                 free_schedule.append(Interval(emp_schedule[i].end, emp_schedule[i+1].start))
#             free_schedule.append(Interval(emp_schedule[-1].end, float("inf")))
#             return free_schedule
#
#         def overlap(interval1, interval2):
#             return not (interval1.start > interval2.end or interval1.end < interval2.start)
#
#         def merge_time(common_free_time, emp_free_time):
#             i = j = 0
#             m = len(common_free_time)
#             n = len(emp_free_time)
#             free_time = []
#
#             while i < m and j < n:
#                 if not overlap(common_free_time[i], emp_free_time[j]):
#                     if common_free_time[i].end < emp_free_time[j].start:
#                         i += 1
#                     else:
#                         j += 1
#                 else:
#                     free_time.append(Interval(max(common_free_time[i].start, emp_free_time[j].start),
#                                               min(common_free_time[i].end, emp_free_time[j].end)))
#                     if common_free_time[i].end == emp_free_time[j].end:
#                         i += 1
#                         j += 1
#                     elif common_free_time[i].end < emp_free_time[j].end:
#                         i += 1
#                     else:
#                         j += 1
#
#             return free_time
#
#         emp_free_time = [free_time(s) for s in schedule]
#
#         free_time = emp_free_time[0]
#
#         for i in range(1, len(emp_free_time)):
#             free_time = merge_time(free_time, emp_free_time[i])
#
#         ans = []
#         for interval in free_time:
#             if interval.start == float("-inf") or interval.end == float("inf") or interval.start == interval.end:
#                 continue
#             ans.append(interval)
#
#         return ans
