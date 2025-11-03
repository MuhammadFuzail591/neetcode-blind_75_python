from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
   res = defaultdict(list)
   for s in strs:
       sortedS = ''.join(sorted(s))
       res[sortedS].append(s)
   return list(res.values())

res = groupAnagrams(["eat","tea","tan","ate","nat","bat"])

print(res)