def longest_substring(s:str)->int:
   max_length = 0
   for i in range(len(s)):
      for j in range(i, len(s)):
         max_length = max(max_length, len(set(s[i:j+1])))
         print(set(s[i:j+1]))
   
   print(max_length)


def longest_substring2(s:str) -> int:
   seen = {}
   max_length = 0
   start = 0
   for end in range(len(s)):
      seen[s[end]] = seen.get(s[end], 0) + 1
      while seen[s[end]] > 1:
         seen[s[start]] -= 1
         start += 1
      max_length = max(max_length, end - start + 1)

   print(max_length)
   return max_length

longest_substring2('pwwkew')