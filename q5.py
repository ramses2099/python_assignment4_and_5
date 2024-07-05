# Question 5
def scrabble_score(word):
    '''
     Calculate the word score based on the scrabble rules
     
     Parameters:
     word (str): The word to be scored
     
     Returns:
     score (int): The word score
    '''
    # Points distribution for each letter
    point_sheet = {
        1 : ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
        2 : ['D', 'G'],
        3 : ['B', 'C', 'M', 'P'],
        4 : ['F', 'H', 'V', 'W', 'Y'],
        5 : ['K'],
        8 : ['J', 'X'],
        10 : ['Q', 'Z']
    }

    score = 0
    for letter in word:
        for key, value in point_sheet.items():
            if letter.upper() in value:
                score += key
    return score

def display_title():
    ''' 
        Display the title of the game

        Parameters: None

        Returns: None
    '''
    print("")
    print("Scrabble Score")
    print("")

def play_again():
    ''' 
        Prompt user to play again

        Parameters: None

        Returns: None
    '''
    again = input("Play again? (y/n) ")
    if again.lower() == 'y':
        game_process()
    elif again.lower() == 'n':
        print("Bye!")
        exit()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        print("")
        play_again()

def game_process():
    '''
        User input and output for the game

        Parameters: None

        Returns: None
    '''
    while True:
        word = input("Enter a word: ")
        score = scrabble_score(word)
        print(word, "is worth", score, "points.")
        print("")
        play_again()


def main():
    display_title()
    game_process()

if __name__ == "__main__":
    main()