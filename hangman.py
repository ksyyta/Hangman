""" 
1. Get word
2. Display empty letter boxes and live count
3. Get letter
    3.1 check if letter is present in word
        3.1.1 if present - display letter in all its place
        3.1.2 if not - updade live count and display message about mistake
4. End game
    4.1 if live count is 0 - you lose
    4.2 in all letters guessed - you win

"""

def main():
    word = input('Give me word\n').lower()
    lives = 5

    guessed_letters = dict()
    for index, letter in enumerate(word):
        if index == 0:
            guessed_letters[letter] = True
        else: guessed_letters[letter] = False

    print_in_console(guessed_letters, word, lives)

    game_over = False
    while not game_over:
        letter_input = input('Give me letter: ').lower()
        if letter_input in word:
            guessed_letters[letter_input] = True
        else: 
            lives -= 1
            print('Wrong letter')

        if lives < 1:
            game_over = True
            print('WASTED')
            break
        
        print_in_console(guessed_letters, word, lives)
        if check_player_won(guessed_letters):
            game_over = True
            print('You won')
            break

def check_player_won(guessed_letters):
    player_won = True    
    for element in guessed_letters.values():
        if element == False:
            player_won = False
            break

    return player_won

def print_in_console(guessed_letters, word, lives):
        output = ""
        for index, letter in enumerate(word):
            if index == 0:
                output += letter.upper() + ' '
            elif guessed_letters[letter] == True:
                output += letter + ' '
            else: output += '_ '

        print(output)
        print(f'Lives: {lives}')

if __name__ == '__main__':
    main()