def decode_string(s:str)-> str:
   stack = []
   currNumber = 0
   currString = ""

   for char in s:
      if char == '[':
         stack.append(currString)
         stack.append(currNumber)
         currString = ""
         currNumber = 0
      elif char == ']':
         num = stack.pop()
         prevString = stack.pop()

         currString = prevString + num * currString

      elif char.isdigit():
         currNumber = currNumber * 10 + int(char)

      else:
         currString += char 
   return currString

decode_string("3[a]2[bc]")