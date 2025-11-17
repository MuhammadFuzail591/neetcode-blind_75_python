def threeSum(nums: list[int]) -> list[list[int]]:
   result = []
   
   for i in range(len(nums)):
      for j in range(i + 1,len(nums)):
         for k in range(j +1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0 and i!=j!=k:
               result.append(sorted([nums[i],nums[j],nums[k]]))

   unique_tuples = set(tuple(inner_list) for inner_list in result)
   unique_list = [list(t) for t in unique_tuples]
   
   return unique_list


def threeSum2(nums:list[int])-> list[list[int]]:
   print(sorted(nums))


threeSum2([-1,0,1,2,-1,-4])

