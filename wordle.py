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
    for attempts in range(1,6):
        guess = input().lower()
        if len(guess) != 5:
            print("Please put a 5 letter word")
            #prevents the attempt from going up since the word is not 5 letters
            continue    
        #if user input === word print "You got the word",  if user input !== word print "Guess again"   
        elif guess == word:
            print("You got the word!")
            break
        else: 
            print("Guess again")
            attempts += 1



user_guess()