def merge(intervals: list[list[int]]) -> list[list[int]]:

   sorted_intervals = sorted(intervals,key = lambda a:a[1])
   merged = []

   for i in range(len(intervals)):
      if len(merged) == 0 or sorted_intervals[i][0] > merged[len(merged) - 1][1]:
         merged.append(sorted_intervals[i])
      else:
         merged[len(merged) - 1][1] = max(sorted_intervals[i][1],merged[len(merged) - 1][1])

   return merged


merge([[1,3],[15,18],[8,10],[2,6]])