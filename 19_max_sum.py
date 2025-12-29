def maximumSubarraySum(nums:list[int], k:int) -> int:
   seen = set()
   state = 0
   start = 0
   max_sum = 0

   for end in range(len(nums)):
      while nums[end] in seen:
         seen.remove(nums[start])
         state -= nums[start]
         start += 1
      
      seen.add(nums[end])
      state += nums[end]

      if end - start + 1 == k:
         max_sum = max(max_sum, state)
         seen.remove(nums[start])
         state -= nums[start]
         start += 1
   return max_sum


maximumSubarraySum([1,1,1,7,8,9],3)