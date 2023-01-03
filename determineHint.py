import random

def determineHint(guess, code):


  newGuess = list(guess)
  newCode = list(code)
  
  defaultList = []

  # Count the number of correct colors in the correct position
  correct_color_and_position = 0
  correct_color_wrong_position = 0

  
  for i in range(len(newGuess)):
    if newGuess[i] == newCode[i]:
      correct_color_and_position += 1
      # Remove the correct pegs from the lists so we don't count them again
      newGuess[i] = ""
      newCode[i] = ""

      
  # Count the number of correct colors in the wrong position
  
  for i in range(len(newGuess)):
    if newGuess[i] != "":
      if newGuess[i] in code:
        correct_color_wrong_position += 1
        newCode[newCode.index(newGuess[i])] = ""

  for i in range(correct_color_and_position):
    defaultList.append("X")
  for i in range(correct_color_wrong_position):
    defaultList.append("O")

  while len(defaultList) < 4:
    defaultList.append("-")


  #print("original " + str(defaultList))
  random.shuffle(defaultList)

  print("Hint: " + ' '.join(defaultList) + "\n")