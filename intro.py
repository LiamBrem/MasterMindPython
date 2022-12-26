import time

def introSequence():
  print("Welcome to Mastermind")
  time.sleep(2)
  print("The goal is very simple")
  time.sleep(3)
  print("There is a secret code I have created")
  time.sleep(3)
  print("And you have 10 attempts to guess it\n")
  
  time.sleep(3)
  print("The secret code is a sequence of 4 numbers, each 1-4")
  print("Such as: [3,2,4,1]")
  time.sleep(4)
  print("However some numbers can be repeated")
  print("Such as: [4,2,4,1]\n")
  time.sleep(4)

  print("On each of your 10 turns, you will input 4 numbers \nthat you think the code could be")
  time.sleep(4)
  print("You will enter the code like this: \"1 2 3 4\" \nwith spaces in betweeen each number\n")
  time.sleep(4)

  print("Then I will return to you a list")
  time.sleep(3)
  print("It may look like this: X--O")
  time.sleep(3)
  print("The O means that you have one right number, but not in the right position")
  time.sleep(4)
  print("The X means that you have 1 right number in the right position")
  time.sleep(4)
  print("It's important to remember that the positions of these in the list do not correspond to the posisitions of the numbers in the final code\n")
  time.sleep(6)

  print("GOOD LUCK!")
  time.sleep(1)
  print("Please Make Your First Guess\n")
  