import random


def determineHint(guess, secret):

  newGuess = list(guess)
  newSecret = list(secret)

  defaultList = []

  # Count the number of correct colors in the correct position
  correct_color_and_position = 0
  correct_color_wrong_position = 0

  guess_copy = newGuess.copy()
  secret_copy = secret.copy()

  for i in range(len(newGuess)):
    if newGuess[i] == newSecret[i]:
      correct_color_and_position += 1
      # Remove the correct pegs from the lists so we don't count them again
      guess_copy.remove(newGuess[i])
      secret_copy.remove(newSecret[i])
      
      #newGuess[i] = ""
      #newCode[i] = ""

  # Count the number of correct colors in the wrong position

  for i in range(len(guess_copy)):
    if guess_copy[i] in secret_copy:
      correct_color_wrong_position += 1

      secret_copy.remove(guess_copy[i])
      #newCode[newCode.index(newGuess[i])] = ""

  for i in range(correct_color_and_position):
    defaultList.append("X")
  for i in range(correct_color_wrong_position):
    defaultList.append("O")

  while len(defaultList) < 4:
    defaultList.append("-")

  

  #print("original " + str(defaultList))
  random.shuffle(defaultList)

  print("Hint: " + ' '.join(defaultList) + "\n")
