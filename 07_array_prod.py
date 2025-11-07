def productExceptSelf(nums: list[int]) -> list[int]:
   res = [1] * len(nums)

   prefix = 1
   for i in range(len(nums)):
      res[i] = prefix
      prefix *= nums[i]

   postfix = 1
   for i in range(len(nums)-1,-1, -1):
      res[i] *= postfix
      postfix *= nums[i]

   return res

# My solution
# from functools import reduce
# def productExceptSelf(nums: list[int]) -> list[int]:
#    result_arr = []
#    for num in range(len(nums)):
#       arr2 = list(nums)
#       arr2.pop(num)
#       product = reduce(lambda acc, val: acc * val, arr2, 1)
#       result_arr.append(product)

#    return result_arr

res = productExceptSelf([1,2,3,4])
print(res)