# Joachim //w//

from random import choice
from termcolor import colored
import sys

def main_menu():
    print('Play Wordle!')
    print('Type a 5 letter Word')

def read_random_words():
    with open("sgb-words.txt") as word:
        words = word.read().splitlines()
        selected_word = choice(words)
        return selected_word

play_again = ''

while play_again != 'n':
    main_menu()
    selected_word = read_random_words()
    print(selected_word) # cheatcode, delete later
    for attempts in range(1, 7):
        while True:
            guess = input().lower()
            if len(guess) < 5:
                print(colored('Retry! Word less than 5 letters long', 'red'))
            else:
                break

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == selected_word[i]:
                print(colored(guess[i], 'green'), end='')
            elif guess[i] in selected_word:
                print(colored(guess[i], 'yellow'), end='')
            else:
                print(colored(guess[i], 'red'), end='')
            
        if guess == selected_word:
            if attempts == 1:
                    print(colored(f'\nCongratulations! You guessed the correct word in {attempts} attempt', 'red'))
            else:
                    print(colored(f'\nCongratulations! You guessed the correct word in {attempts} attempts', 'red'))
            break
        elif attempts == 6:
             print(f'The word was.. {selected_word}')
    play_again = input('Play Again? Y(Yes) N(No) ').lower()