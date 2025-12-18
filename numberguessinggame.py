secret = 7 #7 is stored in the variable secret

attempts = 0 #attempts var is used to count how many times user tries to guess the number

while True: #loop until correct numeber is guessed

    guess = int(input("Guess number:")) #take user input
    attempts += 1 #increase attempts by 1

    if guess == secret: 
        print("correct! attempt:", attempts)
        
        break #stop the loop if guessed correctly