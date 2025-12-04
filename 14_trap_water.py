def trap(height:list[int])-> int:
   if len(height) <=0:
      return 
   left = 0
   right = len(height) -1
   leftMax = height[left]
   rightMax = height[right]
   count =0

   while left<right:
      if height[left] <= height[right]:
         left +=1

         if leftMax <= height[left]: leftMax = height[left]
         else: count += leftMax - height[left]
      else:
         right -=1
         if rightMax <= height[right]: rightMax = height[right]
         else: count += rightMax -height[right]
   
   return count

print(trap([4,2,0,3,2,5]))