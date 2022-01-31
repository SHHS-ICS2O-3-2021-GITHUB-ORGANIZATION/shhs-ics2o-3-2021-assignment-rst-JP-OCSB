# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Trivia Game
# DATE OF CREATION:  Jan 27, 2022
# PURPOSE OF PROGRAM:  To ask a user a series of triva questions than tell them how they did in comparison to the average user
 
# VARIABLE DEFINITION
 
userInput = 0
finalMark = 0
userPercentage = 0
averageScore = 0
 
# INPUT
 
selection = input("Welcome to the trivia game! Please make your genre selection, type math for the math genre or type general for a general genre: ")
 
while selection == "general":
  averageScore = 66
  selection = 0
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
 
  #Repeat the question structure above for the rest of the questions
 
  userInput = input("\n2. When was the computer first invented?:\na) between 1822 and 1832\nb) between 1902 and 1908\nc) between 1833 and 1871\nd) between 1894 and 1902\nPlease enter either a, b, c or d here: ")
  if userInput == "c":
    print("\nCORRECT")
    finalMark = finalMark + 1
  elif userInput != "c":
    print("\nINCORRECT\nThe correct answer was c")
 
  userInput = input("\n3. How many teeth are in the adult mouth including widom teeth?:\na) 25\nb) 22\nc) 43\nd) 32\nPlease enter either a, b, c or d here: ")
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

  userInput = input("\n12. Which river flows through London England?:\na) The Thames\nb) The Ganges\nc) The Nile\nd) The Danube River\nPlease enter either a, b, c or d here: ")
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
 
  userInput = input("\n14. What is the name of the longest river in South America?:\na) The Amazon River\nb) The Nile\nc) The Rhine River\nd) The Volga River\nPlease enter either a, b, c or d here: ")
  if userInput == "a":
    print("\nCORRECT")
    finalMark = finalMark + 1
  elif userInput != "a":
    print("\nINCORRECT\nThe correct answer was a")
 
  userInput = input("\n15. What is the rarest M&M color?:\na) Blue\nb) Red\nc) Brown\nd) Yellow\nPlease enter either a, b, c or d here: ")
  if userInput == "c":
    print("\nCORRECT")
    finalMark = finalMark + 1
  elif userInput != "c":
    print("\nINCORRECT\nThe correct answer was c")
 
  #Printing the amount of questions the user answered correctly
  print("\nYou got " + str(finalMark) + " out of 15 right")
 
  #Calculating the user's percentage
  userPercentage = (float(finalMark) / 15)*100
 
  #Getting rid of the decimal on the user's percentage
  userPercentage = int(userPercentage)
 
  #Printing the user's percentage
  print("\nYour percentage is " + str(userPercentage) + "%")
 
  #Converting user's percentage back to an integer for comparisons below
  userPercentage == int(userPercentage)
 
  #Seeing if user's score is equal to the average score
  if userPercentage == averageScore:
    print("You scored the same as the average user")
 
  #Seeing if user's score is better than the average score
  elif userPercentage > averageScore:
    print("You scored higer than the average user")
 
  #Seeing if user's score is worse than the average score
  elif userPercentage < averageScore:
    print("You scored less than the average score")
 
  #Telling the user the average score of other users
  print("The average score is 66% (10 out of 15)")

 
while selection == "math":
 
 averageScore = 75
 selection = 0
 #Prompting user to start the game
 foo = input("Welcome to the math trivia game!\nI will ask you 8 math questions and at the end I will tell you how many you got right and wrong as well as how your score compares to other people.\nPress enter to start the game!")
 
 # PROCESSING/OUTPUT
 
 #Asking questions
 userInput = int(input("\n1. What is 12 + 72?:\nPlease enter your answer with no spaces just the number here: "))
 #Checking if user is correct
 if userInput == 84:
   print("\nCORRECT")
   #If user is correct add 1 to their score
   finalMark = finalMark + 1
 if userInput != 84:
   #If user is incorrect tell them the right answer
   print("\nINCORRECT\nThe correct answer was 84")
 
 #Repeat the question structure above for the rest of the questions
 
 userInput = int(input("\n2. What is 15 - 7?:\nPlease enter your answer with no spaces just the number here: "))
 if userInput == 8:
   print("\nCORRECT")
   finalMark = finalMark + 1
 if userInput != 8:
   print("\nINCORRECT\nThe correct answer was 8")
 
 userInput = int(input("\n3. What is 135 + 37?:\nPlease enter your answer with no spaces just the number here: "))
 if userInput == 172:
   print("\nCORRECT")
   finalMark = finalMark + 1
 if userInput != 172:
   print("\nINCORRECT\nThe correct answer was 172")
 
 userInput = int(input("\n4. What is 12 x 2?:\nPlease enter your answer with no spaces just the number here: "))
 if userInput == 24:
   print("\nCORRECT")
   finalMark = finalMark + 1
 if userInput != 24:
   print("\nINCORRECT\nThe correct answer was 24")
 
 userInput = int(input("\n5. What is 34 divided 2?:\nPlease enter your answer with no spaces just the number here: "))
 if userInput == 17:
   print("\nCORRECT")
   finalMark = finalMark + 1
 if userInput != 17:
   print("\nINCORRECT\nThe correct answer was 17")
 
 userInput = int(input("\n6. What is 20 divided 4?:\nPlease enter your answer with no spaces just the number here: "))
 if userInput == 5:
   print("\nCORRECT")
   finalMark = finalMark + 1
 if userInput != 5:
   print("\nINCORRECT\nThe correct answer was 5")
 
 userInput = int(input("\n7. What is 31 x 4?:\nPlease enter your answer with no spaces just the number here: "))
 if userInput == 124:
   print("\nCORRECT")
   finalMark = finalMark + 1
 if userInput != 124:
   print("\nINCORRECT\nThe correct answer was 124")
 
 userInput = int(input("\n8. What is 112 + 23?:\nPlease enter your answer with no spaces just the number here: "))
 if userInput == 135:
   print("\nCORRECT")
   finalMark = finalMark + 1
 if userInput != 135:
   print("\nINCORRECT\nThe correct answer was 135")
 
 #Printing the amount of questions the user answered correctly
 print("\nYou got\n " + str(finalMark) + " out of 8 right")
 
 #Calculating the user's percentage
 userPercentage = (float(finalMark) / 8)*100
 
 #Getting rid of the decimal on the user's percentage
 userPercentage = int(userPercentage)
 
 #Printing the user's percentage
 print("\nYour percentage is " + str(userPercentage) + "%")
 
 #Converting user's percentage back to an integer for comparisons below
 userPercentage == int(userPercentage)
 
 #Seeing if user's score is equal to the average score
 if userPercentage == averageScore:
   print("You scored the same as the average user")
 
 #Seeing if user's score is better than the average score
 if userPercentage > averageScore:
   print("You scored higher than the average user")
 
 #Seeing if user's score is worse than the average score
 elif userPercentage < averageScore:
   print("You scored less than the average score")
 
 #Telling the user the average score of other users
 print("The average score is 75% (6 out of 8)")
