def sortColors(nums:list[int]):
   for i in range(len(nums)):
      for j in range(i+1, len(nums)):
         if nums[i] > nums[j]:
            nums[j],nums[i] = nums[i],nums[j]

   print(nums)


def sortColors2(nums:list[int]):

   i = 0
   left = 0
   right = len(nums) -1

   while i<=right:
      if nums[i] == 0:
         nums[i],nums[left] = nums[left], nums[i]
         left +=1
         i +=1
      elif nums[i] == 2:
         nums[i],nums[right] = nums[right], nums[i]
         right -=1
      else:
         i +=1
   
   print(nums)


sortColors2([2,1,2,0,1,0,1,0,1])