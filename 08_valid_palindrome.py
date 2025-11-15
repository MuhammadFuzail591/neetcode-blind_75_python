def isPalindrome(s: str) -> bool:
   
   newStr = ("".join(filter(str.isalnum, s))).lower()
   result_string = ""

   for char in newStr:
      result_string = char + result_string
   
   return result_string == newStr


def isPalindrome2(s:str) -> bool:
   newStr = ""
   for char in s:
      if char.isalnum():
         newStr += char.lower()
   
   return newStr == s[::-1]


isPalindrome2("tab a cat")