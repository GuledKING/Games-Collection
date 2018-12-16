import random
import string

words = ['apple', 'lemon', 'pineapple', 'banana', 'orange', 'strawberry', 'rasberry', 'kiwi', 'starfruit', 'watermelon', 'grapes']
chars = list(string.ascii_lowercase)

def hangman(lives = 6):
    word = random.choice(words)
    mystery_word = ''
    letter_list = []
    for letter in range(len(word)):
        letter_list.append(word[letter])
        mystery_word += '-'
    print(mystery_word)
    while True:
        if lives != 0 and len(letter_list) != 0:
            user_guess = input('Enter a letter. ')
            user_guess = user_guess.lower()
            if user_guess == word:
                print('You guessed correctly! Well played!')
                letter_list = []
            elif user_guess not in chars:
                print('That is not a letter. Try again. ')
            else:
                if user_guess not in letter_list:
                    print(user_guess + ' is not in the word.')
                    lives -= 1
                    print('You now have ' + str(lives) + ' lives left.')
                else:
                    print(user_guess + ' is in the word ' + str(word.count(user_guess)) + ' times.')
                    for letter in range(len(word)):
                        if word[letter] == user_guess:
                            letter_list.remove(word[letter])
                            mystery_l = mystery_word[letter]
                            mystery_word = mystery_word[:letter] + mystery_word[letter].replace('-', word[letter]) + mystery_word[letter+1:len(word)+1]
                        else:
                            pass
                print(mystery_word)
        elif len(letter_list) == 0:
            print('You win!')
            break
        else:
            print('You lost!')
            break
    repeat = input('Play again? (Y/N) ')
    while True:
        if repeat.upper() == 'Y':
            hangman()
        elif repeat.upper() == 'N':
            break
        else:
            print('That is not a valid response. ')   

hangman()