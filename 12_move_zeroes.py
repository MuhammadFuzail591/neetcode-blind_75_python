def moveZeroes(nums:list[int]):
   # nums.sort()

   for i in range(len(nums)):
      for j in range(i+1, len(nums)):
         if nums[i] == 0:
            nums[i],nums[j] = nums[j],nums[i]

   print(nums)

moveZeroes([2,0,4,0,9])
