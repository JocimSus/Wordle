from random import choice
from termcolor import colored

def main_menu():
    print('Play Wordle!')
    print('Type a 5 letter Word')

def read_random_words():
    with open("sgb-words.txt") as word:
        words = word.read().splitlines()
        selected_word = choice(words)
        return selected_word

main_menu()
selected_word = read_random_words()
print(selected_word)

for attempts in range(1, 7):
    while True:
        guess = input().lower()
        if len(guess) < 5:
            print(colored('Retry! Word less than 5 letters long', 'red'))
        else:
            break

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