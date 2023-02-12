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
    # words_list = read_words_in_text()
    while attempts != max_attempts:
        guess = input().lower()
        if len(guess) != 5:
            print("Please put a 5 letter word")
            #prevents the attempt from going up since the word is not 5 letters
            continue    
        #if user input === word print "You got the word",  if user input !== word print "Guess again" 
        # if guess not in words_list:
        #     print("This word doesn't exist")
        #     continue
        elif guess == word:
            print("You got the word!")
            break
        #if the new guess is inside the array, user 
        elif guess in previous_guesses:
            print("You already tried this word.")
            continue
        else: 
            display_word = ""
            #highlighting the letter index of the word
            # none highlights red
            # orange highlights the letter is present but at the wrong index
            # green highlights the letter is present and at the wrong index
            for i in range(len(word)):
                if word[i] == guess[i]:
                    display_word += "\033[1;32m" + word[i] + "\033[0m" 
                elif guess[i] in word:
                    display_word += "\033[1;33m" + guess[i] + "\033[0m"
                else:
                    display_word += "\033[1;31m" + guess[i] + "\033[0m"
            print(display_word)
            print("Guess again.")
            previous_guesses.append(guess)
            attempts += 1
            if attempts == 5:
                print("Game Over!")
                break

user_guess()