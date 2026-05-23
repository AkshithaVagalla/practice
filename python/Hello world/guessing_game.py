secret_number = 9 
count = 0 # this is the number of guesses the user has made
guess_limit = 3 # this is the maximum number of guesses the user can make
while count < guess_limit:
    guess = int(input("guess the number: "))
    count = count + 1 # you can also write this as count += 1
    if guess == secret_number:
        print("you won!")
        break # this will exit the loop if the user guesses the number correctly
else:
    print("sorry, you failed!") # this will be executed if the user fails to guess the number within the guess limit    
        
