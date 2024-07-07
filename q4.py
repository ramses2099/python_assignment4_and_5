#! ./env/bin/ python
from typing import List
from os import system
import random

# Question-4. This exercise examines the process of identifying the maximum value in a collection of
# integers. Each of the integers will be randomly selected from the numbers between 1 and 100.
# The collection of integers may contain duplicate values, and some of the integers between 1 and 100
# may not be present.
# Specifications
# Use randrange and import the relative python library to generate the random numbers

def random_collection(size: int)-> list:
    '''
        Function random_collection for generate random collection of numbers

        Parameters: size: int

        Returns: list
    '''
    random_integers = [random.randrange(1, 101) for _ in range(size)]
    return random_integers

def main():
    print("")
    # input
    size = int(input("Enter the size of collection: "))
    collection = random_collection(size) 
    # Identify the maximum value in the collection
    max_value = max(collection)
    # Print the collection and the maximum value
    print("Collection of random integers:", collection)
    print("Maximum value in the collection:", max_value)   
    
if __name__ == "__main__":
    main()