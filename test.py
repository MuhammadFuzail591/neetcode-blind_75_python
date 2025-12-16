def new_func(fruits):
   max_len = 0
   for i in range(len(fruits)):
      for j in range(i+1,len(fruits)+1):
         subset = set(fruits[i:j])
         if len(subset)<=2:
            max_len = max(max_len, j - i)
   return max_len

new_func([3,3,2,1,2,1,0])