#! ./env/bin/ python
from typing import List
from os import system
import statistics

def display_welcome():
    print()
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
            try:
                score = int(score)
                if score >= 0 and score <= 100:
                    data.append(score)                    
                else:
                    print("Test score must be from 0 through 100. " +
                        "Score discarded. Try again.")
            except ValueError:
                    print("Invalid input. Please enter a number.")


# 4. Modify the process_scores() function so the scores list is its only argument. 
# Then, this function should use a for statement to total the scores in the list.
# It should use the len()function to get the number of scores in the list. 
# And it should get the average by dividing the total scores by the length.
def process_scores(list_score: List) -> None:
    elem_count = len(list_score)
    if elem_count > 0:
        score_total = sum(list_score)
        count = elem_count
        average = round((score_total / count), 2)
        minimum = min(list_score)
        maximum = max(list_score)
        stdev = round((statistics.stdev(list_score)), 2)
        
        # Calculate median
        sorted_scores = sorted(list_score)
        if elem_count % 2 == 1:
            median = sorted_scores[elem_count // 2]
        else:
            median = (sorted_scores[elem_count // 2 - 1] + sorted_scores[elem_count // 2]) / 2
        
        # Calculate mode (if exists)
        try:
            mode = statistics.mode(list_score)
        except statistics.StatisticsError:
            mode = "No unique mode"
        
        # Print all statistics
        print()
        print("Score total:       ", score_total)
        print("Number of Scores:  ", count)
        print("Average Score:     ", average)
        print("Minimum Score:     ", minimum)
        print("Maximum Score:     ", maximum)
        print("Median Score:      ", median)
        print("Mode:              ", mode)
        print("Standard Deviation:", stdev)
    else:
       print()
       print("No input score for calculation") 

# 5. Modify the main () function so the list that's returned by the get_scores() function is
# stored in a variable. Then, modify the call to the process_scores() function so it passes
# just the scores list to it.
def main():
    display_welcome()
    list_score = get_scores() # return list
    process_scores(list_score) # recive a list for process
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


