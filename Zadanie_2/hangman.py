from operator import le
import random as randx
import os

class Game():

    def __init__(self, player_count):
        self.player_count = player_count

    def _play(self):
        print("Game has begun!")

class Hangman(Game):

    def __init__(self, player_count, diff):
        super().__init__(player_count)
        self.difficultie = diff
        self.word = ""
        self.word_list = ['dog','cat','mause','house', 'random', 'apple']

    def word_dashed(self):
        self.word_dashed = []
        for i in range(len(self.word)):
             self.word_dashed.append('_')
        return ''.join(self.word_dashed)

    def getWord(self):
        if self.player_count == 2:
            print("Type word!")
            self.word = str(input()).lower()
            os.system('CLS')
            print("Word typed!")
        else:
            self.word = randx.choice(self.word_list)

    def _game(self):
        print('Game started!')
        tries = self.difficultie
        self.getWord()
        self.word_dashed()
        guessed_word = list(self.word_dashed)
        while tries > 0:
            if ''.join(guessed_word) == self.word:
                print("You win!")
                break
            print('you got '+ str(tries) + ' wrong tries!')
            letter = input('Guess a letter > \n').lower()
            if letter.isalpha():
                if letter in self.word:
                    print('Correct!')
                    for i in range(len(self.word)):
                        if list(self.word)[i] == letter:
                            guessed_word[i] = letter
                    print(''.join(guessed_word))
                elif letter not in self.word:
                    print('Wrong!')
                    tries -= 1
                if tries == 0:
                    print('You lost!')
            else:
                print('Ops... That\'s not a letter, try again!')
class Diff():
    hard = 4
    medium = 6
    easy = 8

Hangman(1, Diff.easy)._game()