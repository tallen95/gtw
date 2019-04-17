import random


replay = True
while replay == True:
    word_list = ["hello", "goodbye","allow","almost","alone","along","deep","defense",
                "degree","democrat","democratic"]
             
    #Picks a random word from the list         
    word = word_list[random.randint(0,len(word_list)-1)]    
    count = 0
    isComplete = False
    
    #Creates the underscores for the word
    correct_letters = [" _ "] * len(word)
    #Creates an empty list for letters the user chooses
    letters_used = [" "] * 100
    incCount = 0
    n = 0   
    string = "Guess the word"
    title = string.center(24)
    
    print(title)
    print(" ")
    print("Guess the word without making five incorrect guesses. ")
    #Prints the underscores 
    print("".join(map(str,(correct_letters))))
        
    #Loops as long as word is not complete and tgere are less than 5 incorrect guesses    
    while isComplete == False and incCount < 5:
        #User guesses a letter
        letterGuess = (input("Guess a letter: "))
        #If duplicate guess, prompt user to choose another
        if letterGuess in letters_used:
                print("You have already guessed this letter, pick another.")
        #If guess is not duplicate do this        
        else:
            #add letter to list of "used letters"
            letters_used[n] = letterGuess
            n= n+1
            
            for i in range(len(word)):
                
                
                #checks if letter is in word
                if letterGuess is word[i]:
                    #adds letter in place if underscore
                    correct_letters[i] = word[i]
                    #checks how many correct letters there are
                    if correct_letters is not " _ ":
                        count +=1
                        #checks if word is complete
                        if len(word) == count:
                            isComplete = True
                            break
                        
                        else:
                            continue
                         
                    else:
                        
                        continue
                #if guess is incorrect, prompt user they are incorrect
                if letterGuess not in word:
                     print(" ")
                     print("Incorrect")
                     #counts number of incorrect guesses
                     incCount = incCount+1
                     break
            
                
                
            
        
        #prints current guessed word
        print("".join(map(str,(correct_letters))))
        print(" ")
        #prints how many incorrect guesses
        print("Incorrect guesses: ",incCount)
        print(" ")
        #shows what letters have been used
        print("Letters used:")
        print("".join(map(str,(letters_used)))) 
    #checks for completed word
    if isComplete == True:    
        print("You win!!")
        print(" ")
        print(" ")
        v = True
        
        #loops until you get a valid response (Y/N)
        while v == True:
            #asks if user would like to play again
            userIn = input("Would you like to play again? (Y/N)")
            #if yes, replay
            if userIn.lower() == "y":
                replay = True
                break
            #if no, thank user for playing
            if userIn.lower() == "n":
                replay = False
                print("Thank you for playing!")
                break
            #if response if invalid, ask for a new response
            else:
                print("Invalid response, please enter Y or N.")
                v = True
        #if game is over, break out of loops   
        if replay == False:           
            break
        #if user wants to replay, continue to loop through
        else:
            continue
        #break to first while        
        break

    else:
        print("You lose")  
        print("The correct word was: ", word)
        print(" ")
        print(" ")
        v = True
        
        #loops until you get a valid response (Y/N)
        while v == True:
            #asks if user would like to play again
            userIn = input("Would you like to play again? (Y/N)")
            #if yes, replay
            if userIn.lower() == "y":
                replay = True
                break
            #if no, thank user for playing
            if userIn.lower() == "n":
                replay = False
                print("Thank you for playing!")
                break
            #if response if invalid, ask for a new response
            else:
                print("Invalid response, please enter Y or N.")
                v = True
        #if game is over, break out of loops   
        if replay == False:           
            break
        #if user wants to replay, continue to loop through
        else:
            continue
        
            
    
       

            
            
    
        
        
    
