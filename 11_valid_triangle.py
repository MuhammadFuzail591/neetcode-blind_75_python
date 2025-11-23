def triangleNumber(nums:list[int]) -> int:
   nums.sort()
   result=[]
   for i in range(len(nums) - 2):
      for j in range(i+1,len(nums)-1):
         for k in range(j+1, len(nums)):
            if nums[i] + nums[j] > nums[k]:
               result.append([nums[i], nums[j],nums[k]])
   return len(result)

print(triangleNumber([11,4,9,6,15,18]))