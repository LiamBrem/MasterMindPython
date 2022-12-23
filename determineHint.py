import random

def determineHint(guess, secretCode):
  print("Determine hint " + str(secretCode))
  
  defaultList = []

  # Count the number of correct colors in the correct position
  correct_color_and_position = 0
  for i in range(4):
    if guess[i] == secretCode[i]:
      correct_color_and_position += 1
      # Remove the correct pegs from the lists so we don't count them again
      guess[i] = None
      secretCode[i] = None

  # Count the number of correct colors in the wrong position
  correct_color_wrong_position = 0
  for i in range(4):
    if guess[i] is not None:
      if guess[i] in secretCode:
        correct_color_wrong_position += 1
        secretCode[secretCode.index(guess[i])] = None

  for i in range(correct_color_and_position):
    defaultList.append("X")
  for i in range(correct_color_wrong_position):
    defaultList.append("O")

  while len(defaultList) < 4:
    defaultList.append("-")

  print("Default list " + str(defaultList))

  #print("original " + str(defaultList))
  random.shuffle(defaultList)

  return defaultList