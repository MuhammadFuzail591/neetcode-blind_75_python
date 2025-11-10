def longestConsecutive(nums: list[int]) -> int:
      numSet = set(nums)
      longest = 0

      for num in numSet:
         if (num -1 ) not in numSet:
               length = 1
               while (num + length) in numSet:
                  length += 1
               
               longest = max(length, longest)

      return longest




# def longestConsecutive(nums: list[int]) -> int:
#    sorted_arr = sorted(nums)
#    count = 0
#    for i in range(len(sorted_arr) - 1):
#       if sorted_arr[i] == sorted_arr[i+1] - 1:\
#          count += 1
#    return count + 1
      
        


longestConsecutive([0,3,7,2,5,8,4,6,0,1])