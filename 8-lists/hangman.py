# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'hello',
    'goodbye',
    'code',
    'computer',
    'theme',
    'clear',
    'word',
    'hangman',
    'pencil',
    'ruler',
    'website'
]

def random_word():
    i = random.randint(0, len(WORDS) - 1)
    return WORDS[i]

def display_board(hidden, tries):
    print(IMAGES[tries])
    print('')
    print(hidden)
    print('--- * --- * --- * --- * --- * --- * ---')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Try a letter: '))

        letter_indexes = []

        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
        
        if len(letter_indexes) == 0:
            tries += 1
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter
        
        letter_indexes = []

        # check if the player wins
        if hidden_word.count('-') == 0:
            print('--- * --- * --- * --- * --- * --- * ---')
            print('YOU WIN!!!')
            print('--- * --- * --- * --- * --- * --- * ---')
            break
        # check if player loses
        if tries == len(IMAGES) - 1:
            print('--- * --- * --- * --- * --- * --- * ---')
            print('better luck next time :(, the word was {}'.format(word))
            print('--- * --- * --- * --- * --- * --- * ---')
            break



    

if __name__ == '__main__':
    print('W E L C O M E   T O   H A N G M A N')
    run()
    input('thanks for playing, press enter to exit of the game.')