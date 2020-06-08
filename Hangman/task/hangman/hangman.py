import random
from string import ascii_lowercase


class Hangman:
    def __init__(self):
        self.list_win = ['python', 'java', 'kotlin', 'javascript']
        self.random_word = random.choice(self.list_win)
        self.print_word = ["-"] * len(self.random_word)
        self.tries = 0
        self.already_input = set()
        print("H A N G M A N")

    def input_word(self):
        print()
        print("".join(self.print_word))
        letter = input("Input a letter: ")
        if len(letter) > 1:
            print("You should input a single letter")
        elif letter in ascii_lowercase:
            if letter in self.already_input:
                print("You already typed this letter")
            elif letter not in self.random_word:
                print("No such letter in the word")
                self.already_input.add(letter)
                self.tries += 1
            else:
                self.already_input.add(letter)
                indices = [i for i in range(len(self.random_word)) if self.random_word[i] == letter]
                for index in indices:
                    self.print_word[index] = letter
        else:
            print("It is not an ASCII lowercase letter")

    def check_win(self):
        while self.tries < 8 and "-" in self.print_word:
            self.input_word()
        if self.tries == 8:
            print("You are hanged!")
        if "-" not in self.print_word:
            print("You guessed the word!")
            print("You survived!")

    def start_game(self):
        while True:
            command = input('Type "play" to play the game, "exit" to quit: ')
            if command == "exit":
                break
            elif command == "play":
                self.check_win()


hm = Hangman()
hm.start_game()
