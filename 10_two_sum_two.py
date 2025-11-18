def twoSum(numbers:list[int], target:int) -> list[int]:

   left = 0
   right = len(numbers) -1

   while left<right:
      res = numbers[left] + numbers[right]

      if res == target:
         return [left +1, right+1]
      
      if res < target:
         left +=1
      
      if res > target:
         right -=1

   return []

res = twoSum([-1,0], -1)

print(res)