import random
import intro
from determineHint import determineHint


def generateCode():  # returns code as a list
  code = []
  for i in range(4):
    code.append(random.randint(1, 4))

  return code


def getGuess():  # returns string ("4 2 3 1")
  isGuessInRightFormat = False

  while (isGuessInRightFormat == False):
    guess = input("Guess: ")

    countSpaces = 0
    numsOneFour = 0

    for i in range(len(guess)):
      if i % 2 == 1 and guess[i] == " ":
        countSpaces += 1
      if i % 2 == 0 and int(guess[i]) >= 1 and int(guess[i]) <= 4:
        numsOneFour += 1

    if countSpaces == 3 and numsOneFour == 4:
      isGuessInRightFormat = True
    else:
      print("<did not enter correctly, try again>")

  return guess


def checkRightGuess(guess, secretCode):  #returns bool
  if guess == secretCode:
    return True
  else:
    return False


def endSequence(secretCode, attempts):  # void
  print("\n     CONGRATULATIONS")
  print("You guessed the secret code")
  print("The Secret Code Was " + str(secretCode))
  print("It took you " + str(attempts) + " attempts!")




if __name__ == "__main__":
  secretCode = generateCode()
  intro.introSequence()
  print("ORIGINAL " + str(secretCode))
  
  correct = False
  
  for i in range(10):
    print("FOR" + str(secretCode))
    
    guess = getGuess()
    #guess is now a string
    guess = guess.split()
  
    #this takes it from a list of strings to a list of ints
    guess = list(map(int, guess))
  
    # automatically ends if it's the correct guess
    if checkRightGuess(guess, secretCode) == True:
      endSequence(secretCode, i + 1)
      correct = True
      break
  
    print("Hint: " + ' '.join(determineHint(guess, secretCode)) + "\n")
  
  if correct == False:
    print("\nYou couldn't guess it in time")
    print("The secret code was " + str(secretCode))
