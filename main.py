import random
import argparse

class WordGame(object):
    word = None
    limit = False

    rules = """
Rules
The Code will choose a random word, then tell you the length. The goal is for
you to guess the right word. With each guess, the game will respond with a number 
of 'cows' and number of 'bulls' cows are the correct letters in the word (but in the
wrong place) and bulls are the correct letters in the correct place in the word.
    """

    print("\n {}".format(rules))

    def return_args(self):
        parser = argparse.ArgumentParser(description='Runs the cows and bulls roadtrip game', prog='main')
        parser.add_argument('-l', '--limit', help='limit the length of the word chosen', default=False)
        args = parser.parse_args()
        limit = int(args.limit)
        if limit <= 1:
            limit = 2
            print('no words < 1 character, setting limit to 2')
        self.limit = limit

    def load_words(self):
        with open('words.txt', 'r') as f:
            read_lines = f.read()
            word_list = read_lines.split('\n')

            return word_list

    def initialize(self):
        words = self.load_words()
        limit = self.limit

        if limit:
            words = [word for word in words if len(word) <= limit]

        self.word = (words[random.randint(0, len(words) - 1)]).lower()

    def guess(self, guess):
        answer = self.word
        guess = guess.lower()
        cows = 0
        bulls = 0

        if guess == answer:
            return False

        for index, letter in enumerate(guess):
            if letter == answer[index]:
                bulls += 1
            elif letter in answer:
                cows += 1
        return cows, bulls

    def printWordLenght(self):
        print("I'm thinking of a ... {} letter word".format(len(self.word)))


def main():
    wg = WordGame()
    wg.return_args()
    wg.initialize()
    print('\npress q to quit at any time\n')
    wg.printWordLenght()

    while True:
        user_input = input('\nEnter Your Guess: ')
        if len(str(user_input)) > len(wg.word):
            print('Your Guess is too long, try a word with {} letters'.format(len(wg.word)))
            continue
        elif user_input.lower() == 'q':
            print('come back soon!')
            break
        else:
            results = wg.guess(str(user_input))

        if not results:
            print('Winner!')
            user_restart = input('\nwould you like to play again? (y/n)')
            if user_restart.lower() == 'y':
                wg.initialize()
                wg.printWordLenght()
                continue
            elif user_restart.lower() == 'n':
                break
        else:
            cows, bulls = results
            print('There are {} cows and {} bulls'.format(cows, bulls))


if __name__ == '__main__':
    main()