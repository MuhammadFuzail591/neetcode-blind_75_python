def most_water(height:list[int])-> int:
   maxArea = 0

   for i in range(len(height)):
      for j in range(i+1, len(height)):
         width = j - i
         h = min(height[i],height[j])
         currentArea = width * h

         maxArea = max(maxArea, currentArea)
   return maxArea



def most_water2(height:list[int]) -> int:
   maxArea = 0
   left = 0
   right = len(height) - 1

   while left < right:
      width = right - left
      hgt = min(height[left],height[right])
      currentArea = width * hgt

      maxArea = max(currentArea, maxArea)

      if height[left] < height[right]: left += 1
      else: right -=1

   return maxArea
print(most_water2([4,3,2,1,4]))