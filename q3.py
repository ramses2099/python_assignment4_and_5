#! ./env/bin/ python
from typing import List
from os import system


# Question-3. Create a program that determines and displays the number of unique characters in a
# string entered by the user. For example, Hello, World! has 10 unique characters while zzz has only one
# unique character.
# Specifications
# • Use a dictionary or set to solve this problem.
# • Define a function

def count_unique_characters(input_string:str)->int:
    '''
        Function count_unique_characters for count unique characters

        Parameters: input_string: str

        Returns: int
    '''
    #set to store unique characters
    uni_characters = set(input_string)
    # Return the number of unique characters
    return len(uni_characters)


def main():
    # input
    print()
    print("Unique Character Counter")
    print()
    str_input = input("Enter a string: ")

    # Call the function and display the result
    count = count_unique_characters(str_input)
    print(f"The number of unique characters in the string is: {count}")


if __name__ == "__main__":
    main()