from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
   freq = {}

   for num in nums:
      freq[num] = freq.get(num, 0) + 1
   
   sorted_freq = sorted(freq.items(), key=lambda x:x[1],reverse=True)

   return [num for num, count in sorted_freq[:k]]
   


res = topKFrequent([1,1,1,2,2,3],2)
print(res)