from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
   indices = {}

   for i, n in enumerate(nums):
      indices[n] = i

   for i, n in enumerate(nums):
      difference = target - n
      if difference in indices and indices[difference] != i:
         return [i, indices[difference]]

   return []


print(twoSum([3,4,5,6], 7))