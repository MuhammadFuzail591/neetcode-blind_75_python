def moveZeroes(nums:list[int]):
   # nums.sort()

   for i in range(len(nums)):
      for j in range(i+1, len(nums)):
         if nums[i] == 0:
            nums[i],nums[j] = nums[j],nums[i]

   print(nums)


def moveZeroes2(nums:list[int]):
   nextNonZero = 0
   for i in range(len(nums)):
      if nums[i] != 0:
         nums[nextNonZero],nums[i] = nums[i],nums[nextNonZero]
         nextNonZero +=1


def moveZeroes3(nums:list[int]):
   sIndex =0

   for i in range(len(nums)):
      if nums[i] != 0:
         nums[sIndex] = nums[i]
         sIndex+=1
   
   for i in range(sIndex,len(nums)):
      nums[i] =0

   print(nums)

moveZeroes3([2,0,4,0,9])
