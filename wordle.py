import random

def game_start():
    print("Guess the 5 letter word.")


#opens the words.txt file
def read_words_in_text():
    with open('words.txt') as f:
        #important - splitlines, will return a single word, without splitlines will return all the words
        words = f.read().splitlines()
        return random.choice(words)


game_start()
word = read_words_in_text()

def user_guess():
    #number of tries for user to guess word
    attempts = 0
    #max attempts
    max_attempts = 5
    #array to store attempts of the word
    previous_guesses = []
    while attempts != max_attempts:
        guess = input().lower()
        if len(guess) != 5:
            print("Please put a 5 letter word")
            #prevents the attempt from going up since the word is not 5 letters
            continue    
        #if user input === word print "You got the word",  if user input !== word print "Guess again"   
        elif guess == word:
            print("You got the word!")
            break
        #if the new guess is inside the array, user 
        elif guess in previous_guesses:
            print("You already tried this word.")
            continue
        else: 
            print("Guess again")
            previous_guesses.append(guess)
            attempts += 1
            if attempts == 5:
                print("Game Over!")
                break


user_guess()