def isValid(s:str) -> bool:
   stack = []
   mapping = {")":"(", "}":"{", "]":"["}

   for character in s:
      if(character in mapping):
         if(len(stack)==0 or stack[len(stack) -1] != mapping[character]):
            print(False)
            return False
         stack.pop()
      else:
         stack.append(character)
   print(len(stack) ==0)
   return len(stack) == 0


isValid("()")