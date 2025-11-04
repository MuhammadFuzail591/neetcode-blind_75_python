from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
   initial_set = set(nums)
   result_arr = []
   for i in initial_set:
      res = nums.count(i)
      if res >= k:
         result_arr.append(i)

   return result_arr


res = topKFrequent([1,2],2)
print(res)