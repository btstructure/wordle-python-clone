import random

def game_start():
    print("Guess the 5 letter word.")


#opens the words.txt file
def read_words_in_text():
    with open('words.txt') as f:
        #important - splitlines, will return a single word, without splitlines will return all the words
        words = f.read().splitlines()
        return random.choice(words)

def word_list():
    with open('words.txt') as f:
        words_list = f.read()
        return(words_list)

game_start()
list_of_words = word_list()


def user_guess():
    word = read_words_in_text()
    #number of tries for user to guess word
    attempts = 0
    #max attempts
    max_attempts = 6
    #array to store attempts of the word
    previous_guesses = []
    
    word_counts = {letter: word.count(letter) for letter in word}

    while attempts != max_attempts:
        guess = input().lower()
        guess_counts = {letter: guess.count(letter) for letter in guess}
        if len(guess) != 5:
            print("Please put a 5 letter word")
            #prevents the attempt from going up since the word is not 5 letters
            continue    
        #if user input === word print "You got the word",  if user input !== word print "Guess again" 
        if guess not in list_of_words:
            print("This word doesn't exist")
            continue
        elif guess == word:
            print("You got the word! The word was: " + word + " .")
            print("It took you " + str(attempts) + " attempts!")
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
                    word_counts[word[i]] -= 1 
                elif guess[i] in word_counts and guess_counts[guess[i]] <= word_counts[guess[i]]:
                    display_word += "\033[1;33m" + guess[i] + "\033[0m"
                    word_counts[guess[i]] -= 1
                else:
                    display_word += "\033[1;31m" + guess[i] + "\033[0m"
            print(display_word)
            print("Guess again.")
            previous_guesses.append(guess)
            attempts += 1
            if attempts == 6:
                print("Game Over!")
                print("The word was " + word )
                break

user_guess()


def play_again():
    while True:
        user_input = input("Would you like to play again (y/n): ").lower()
        if user_input == "y":
            read_words_in_text()
            game_start()
            user_guess()
            play_again()
            break
        elif user_input == "n":
            print("Thanks for playing")
            break
        else:
            print("Please type y or n")


play_again()
