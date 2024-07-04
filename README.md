# python_assignment4_and_5
Python assignment 4 and 5

# Question-1.
Use a list for the Test Scores program
In this exercise, you'll modify a Test Scores program that gets the test scores that a user enters and then calculates and displays the average test score. You'll enhance this program by storing the test scores in a list and then getting and displaying other
statistics for the test scores, like this:

1. In PyCharm, open the test_scores.py file that's given on eConestoga
2. Review the code, and test the program.
3. Modify the get_scores() function so the test scores are stored in a list named scores. This list should be returned by the function when all scores have been entered. The function should still make sure that the entries are valid, but the score_total and count variables aren't needed and shouldn't be updated.

4. Modify the process_scores() function so the scores list is its only argument. Then, this function should use a for statement to total the scores in the list. It should use the len()function to get the number of scores in the list. And it should get the average by dividing the total scores by the length.

5. Modify the main () function so the list that's returned by the get_scores() function is stored in a variable. Then, modify the call to the process_scores() function so it passes just the scores list to it.

6. Test this program to make sure everything is working right.

7. Enhance this program by getting and displaying all of the other statistics shown
above. For an odd number of scores, the median score is the score that has the same
number of scores below it as above it. For an even number of scores, calculate the
median by taking the average of the two middle numbers.