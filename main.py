# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Trivia Game
# DATE OF CREATION:  Jan 27, 2022
# PURPOSE OF PROGRAM:  To ask a user a series of triva questions than tell them how they did in comparison to the average user

# VARIABLE DEFINITION
userInput = 0
finalMark = 0
# INPUT

#Prompting user to start the game
foo = input("Welcome to the trivia game!\nI will ask you 15 questions and at the end I will tell you how many you got right and wrong as well as how your score compares to other people.\nPress enter to start the game!")

# PROCESSING/OUTPUT

#Asking questions
userInput = input("\n1. What is the largest ocean called?:\na) Pacific Ocean\nb) Arctic Ocean\nc) Atlantic Ocean\nd) Indian Ocean\nPlease enter either a, b, c or d here: ")
#Checking if user is correct
if userInput == "a":
  print("\nCORRECT")
  #If user is correct add 1 to their score
  finalMark = finalMark + 1
elif userInput != "a":
    #If user is incorrect tell them the right answer
  print("\nINCORRECT\nThe correct answer was a")

userInput = input("\n2. When was the computer first invented?:\na) between 1822 and 1832\nb) between 1902 and 1908\nc) between 1833 and 1871\nd) between 1894 and 1902\nPlease enter either a, b, c or d here: ")
if userInput == "c":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "c":
  print("\nINCORRECT\nThe correct answer was c")

userInput = input("\n3. How many teeth are in the adult mouth?:\na) 25\nb) 22\nc) 43\nd) 32\nPlease enter either a, b, c or d here: ")
if userInput == "d":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "d":
  print("\nINCORRECT\nThe correct answer was d")

userInput = input("\n4. When did world war 1 start and end?:\na) July 28, 1914 to November 11, 1918\nb) September 12, 1923 to January 2, 1926\nc) August 28, 1913 to July 18, to 1917\nd) June 7, 1982 to September 18, 1983\nPlease enter either a, b, c or d here: ")
if userInput == "a":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "a":
  print("\nINCORRECT\nThe correct answer was a")

userInput = input("\n5. How many bones are there in the human body as an adult?:\na) 206\nb) 128\nc) 194\nd) 251\nPlease enter either a, b, c or d here: ")
if userInput == "a":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "a":
  print("\nINCORRECT\nThe correct answer was a")

userInput = input("\n6. Do you have more bones in your body as a kid, or as an adult?:\na) Adult\nb) Kid\nPlease enter either a or b here: ")
if userInput == "b":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "b":
  print("\nINCORRECT\nThe correct answer was b")

userInput = input("\n7. What is the fastest land animal?:\na) Lynx\nb) kangaroo\nc) Cheetah\nd) Hyena\nPlease enter either a, b, c or d here: ")
if userInput == "c":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "c":
  print("\nINCORRECT\nThe correct answer was c")
  
userInput = input("\n8. How many states are there in the U.S?:\na) 34\nb) 61\nc) 52\nd) 50\nPlease enter either a, b, c or d here: ")
if userInput == "d":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "d":
  print("\nINCORRECT\nThe correct answer was d")
  
userInput = input("\n9. How many continents are there in the world?:\na) 7\nb) 8\nc) 5\nd) 10\nPlease enter either a, b, c or d here: ")
if userInput == "a":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "a":
  print("\nINCORRECT\nThe correct answer was a")
  
userInput = input("\n10. How many countries are there in the world?:\na) 234\nb) 195\nc) 182\nd) 89\nPlease enter either a, b, c or d here: ")
if userInput == "b":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "b":
  print("\nINCORRECT\nThe correct answer was b")
  
userInput = input("\n11. In what sport is a shuttlecock used?:\na) Volleyball\nb) Baseball\nc) Soccer\nd) Badminton\nPlease enter either a, b, c or d here: ")
if userInput == "d":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "d":
  print("\nINCORRECT\nThe correct answer was d")
  
userInput = input("\n12. Which river flows through London?:\na) The Thames\nb) The Ganges\nc) The Nile\nd) The Danube River\nPlease enter either a, b, c or d here: ")
if userInput == "a":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "a":
  print("\nINCORRECT\nThe correct answer was a")
  
userInput = input("\n13. Which Italian city is famous for its leaning tower?:\na) Rome\nb) Pisa\nc) Venice\nd) Verona\nPlease enter either a, b, c or d here: ")
if userInput == "b":
  print("\nCORRECT")
  finalMark = finalMark + 1
elif userInput != "b":
  print("\nINCORRECT\nThe correct answer was b")

print("\nYou got\n " + str(finalMark) + " out of 15 right")

userPercentage = (float(finalMark) / 15)*100
userPercentage = int(userPercentage)
print("\nYour percentage is " + str(userPercentage) + "%")