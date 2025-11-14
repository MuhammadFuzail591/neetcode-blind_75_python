def isPalindrome(s: str) -> bool:
   
   newStr = ("".join(filter(str.isalnum, s))).lower()
   result_string = ""

   for char in newStr:
      result_string = char + result_string
   
   return result_string == newStr
   


isPalindrome("tab a cat")