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

# Question-2.


# Question-3.
Create a program that determines and displays the number of unique characters in a
string entered by the user. For example, Hello, World! has 10 unique characters while zzz has only one
unique character.
Specifications
• Use a dictionary or set to solve this problem.
• Define a function

# Question-4. 

This exercise examines the process of identifying the maximum value in a collection of
integers. Each of the integers will be randomly selected from the numbers between 1 and 100.
The collection of integers may contain duplicate values, and some of the integers between 1 and 100
may not be present.
Specifications
Use randrange and import the relative python library to generate the random numbers

# Question-5. 

In the game of ScrabbleTM, each letter has points associated with it. The total score of a
word is the sum of the scores of its letters. More common letters are worth fewer points while less
common letters are worth more points.
The points associated with each letter are shown below:

Write a program that computes and displays the ScrabbleTM score for a word.
Specifications
• Create a dictionary that maps from letters to point values. Then use the
dictionary to compute the score.
• Use a function