import random

print('*********************************')
print('*        Hangman Game           *')
print('*********************************')

word_list = ['java', 'python', 'c', 'c++', 'dart', 'html', 'css',
             'javascript', 'php', 'ruby']
#random words
random_word = random.choice(word_list)



def hangman_figure(attempts):
    hangman_parts = [
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        """
    ]
     
    if attempts == 2 :
        print(hangman_parts[0])
    elif attempts == 1:
        print(hangman_parts[1])
    else:
      print(hangman_parts[2])

def main():
    print('I\'ve picked my favorite programming language!')
    print('Can you guess the letters in it?')
    print('Remember. You only have three chances!')

    attempts = 3
    guessed_word = ['_'] * len(random_word)

    #attempts loop
    while attempts > 0:
        guess = input(f'You have {attempts} chances left. Enter a letter: ')
        
        if len(guess) != 1 or not guess.isalnum():
            print('Please enter a single letter.')
            continue
    
        if guess in random_word:
            print('Good guess!')
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    guessed_word[i] = guess
            print(' '.join(guessed_word))#add letter to guessed word
            if '_' not in guessed_word:
                print('**Congratulations!**\nYou\'ve won the game')
                print(f'My favorite programming language is "{random_word}"')
                break
        else:
            attempts -= 1
            hangman_figure(attempts)
            print(f'Sorry, "{guess}" is not in the word. You have {attempts} chances left.')
        

    if '_' in guessed_word:
        print('Sorry! You have run out of chances. You lost the game.')
        print(f'My favorite programming language is "{random_word}"')


main()