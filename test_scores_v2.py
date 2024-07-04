#!/usr/bin/env python3
from typing import List
from os import system

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")


# 3. Modify the get_scores() function so the test scores are stored in a list named scores.
# This list should be returned by the function when all scores have been entered.
# The function should still make sure that the entries are valid,
# but the score_total and count variables aren't needed and shouldn't be updated.
def get_scores() -> List:
    data = list()
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  data
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                data.append(score)
                
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")


# 4. Modify the process_scores() function so the scores list is its only argument. 
# Then, this function should use a for statement to total the scores in the list.
# It should use the len()function to get the number of scores in the list. 
# And it should get the average by dividing the total scores by the length.
def process_scores(list_score:List)->None:
    elem_count = len(list_score)
    score_total = 0
    count = 0
    average = 0
    if(elem_count > 0):
        # calculate average score
        for n in list_score:
            score_total += n
            count += 1
        
        # calculate average score
        average = score_total / count            
        # format and display the result
        print()
        print("Score total:       ", score_total)
        print("Number of Scores:  ", count)
        print("Average Score:     ", average)
    else:
       print()
       print("No input score for calculation") 

# 5. Modify the main () function so the list that's returned by the get_scores() function is
# stored in a variable. Then, modify the call to the process_scores() function so it passes
# just the scores list to it.
def main():
    system("clear")
    display_welcome()
    list_score = get_scores() # return list
    process_scores(list_score) # recive a list for process
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


