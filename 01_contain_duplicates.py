
def contain_duplicate(nums):

   seen = set()

   for num in nums:
      if num in seen:
         return True
      seen.add(num)

   return False    



def contain_duplicate_2(nums):

   return len(set(nums)) != len(nums)