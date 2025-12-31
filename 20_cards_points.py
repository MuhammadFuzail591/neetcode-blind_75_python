def maxScore(cardPoints: list[int], k: int) -> int:

   total = sum(cardPoints)

   if k >= len(cardPoints):
      return total
   

   start = 0
   state = 0
   max_score = 0

   for end in range(len(cardPoints)):
      state += cardPoints[end]

      if end - start + 1 == len(cardPoints) - k:
         max_score = max(total - state, max_score)
         state -= cardPoints[start]
         start +=1
   print(max_score)
   return max_score


   
maxScore([1,2,3,4,5,6,1],3)