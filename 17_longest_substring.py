def longest_substring(s:str)->int:
   max_length = 0
   for i in range(len(s)):
      for j in range(i, len(s)):
         substring = s[i:j+1]
         if len(substring) == len(set(substring)):
            max_length = max(max_length, len(set(substring)))
   
   print(max_length)


def longest_substring2(s:str) -> int:
   seen = {}
   start = 0
   max_length = 0

   for end in range(len(s)):
      seen[s[end]] = seen.get(s[end],0) +1

      while seen[s[end]] > 1:
         seen[s[start]] -=1
         start +=1

      max_length = max(max_length, end-start+1)

   return max_length


longest_substring('pwwkew')