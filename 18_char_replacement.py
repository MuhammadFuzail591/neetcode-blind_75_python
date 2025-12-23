def character_replacement(s:str, k:int) -> int:
   state = {}
   max_frequency = 0
   max_length = 0
   start = 0


   for end in range(len(s)):
      state[s[end]] = state.get(s[end], 0) + 1
      max_frequency = max(max_frequency, state[s[end]])

      if k + max_frequency < end - start + 1:
         state[s[start]] -=1
         start +=1

      max_length = max(max_length, end - start + 1)
   
   return max_length


character_replacement('AABABBA',2)