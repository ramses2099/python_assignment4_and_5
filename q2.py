#! ./env/bin/ python
from typing import List
from os import system

# Question-2. Use a list to store the players

# Update the program (discussed in class) so it allows you to store the players for the
# starting lineup. This should include the player's name, position, at bats, and hits. In
# addition, the program should calculate the player's batting average from at bats and hits.

valid_positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')  # 2. Use a tuple to store all valid positions
lineup = [] # 1. Use a list to store the players

def display_menu():
    print()
    print("============================================================")
    print("Baseball Team Manager")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("POSITIONS")
    print(", ".join(valid_positions))
    print("============================================================")
    print()

def display_positions():
    print("POSITIONS")
    print(", ".join(valid_positions))

def display_lineup():
    if not lineup:
        print("No players in the lineup.")
    else:
        print("Current lineup:")
        for i, player in enumerate(lineup, start=1):
            name, position, at_bats, hits = player
            average = hits / at_bats if at_bats > 0 else 0
            print(f"{i}. Name: {name}, Position: {position}, At bats: {at_bats}, Hits: {hits}, Batting Average: {average:.3f}")

def add_player():
    name = input("Name: ")
    while True:
        position = input("Position: ")
        if position in valid_positions: # 3. Making sure the position entered is valid
            break
        else:
            print("Invalid position. Try again.")
            display_positions()
    
    while True:
        try:
            at_bats = int(input("At bats: "))
            if at_bats >= 0: # 3. Validating the number of at bats
                break
        except ValueError:
            pass
        print("Invalid entry. At bats must be a non-negative integer.")
    
    while True:
        try:
            hits = int(input("Hits: "))
            if 0 <= hits <= at_bats: # 3. Validating the number of hits
                break
        except ValueError:
            pass
        print("Invalid entry. Hits must be a non-negative integer and cannot exceed at bats.")
    
    lineup.append([name, position, at_bats, hits])
    print(f"{name} was added.")

def remove_player():
    display_lineup()
    try:
        index = int(input("Enter the player number to remove: ")) - 1
        if 0 <= index < len(lineup):
            removed_player = lineup.pop(index)
            print(f"{removed_player[0]} was removed.")
        else:
            print("Invalid player number.")
    except ValueError:
        print("Invalid entry. Please enter a valid player number.")

def move_player():
    display_lineup()
    try:
        old_index = int(input("Enter the player number to move: ")) - 1
        if 0 <= old_index < len(lineup):
            new_index = int(input("Enter the new position in the lineup: ")) - 1
            if 0 <= new_index < len(lineup):
                player = lineup.pop(old_index)
                lineup.insert(new_index, player)
                print(f"{player[0]} was moved to position {new_index + 1}.")
            else:
                print("Invalid new position.")
        else:
            print("Invalid player number.")
    except ValueError: 
        print("Invalid entry. Please enter valid numbers.")

def edit_player_position():
    display_lineup()
    try:
        index = int(input("Enter the player number to edit position: ")) - 1
        if 0 <= index < len(lineup):
            while True:
                position = input("New position: ")
                if position in valid_positions:
                    lineup[index][1] = position
                    print(f"{lineup[index][0]}'s position was updated to {position}.")
                    break
                else:
                    print("Invalid position. Try again.")
                    display_positions()
        else:
            print("Invalid player number.")
    except ValueError:
        print("Invalid entry. Please enter a valid player number.")

def edit_player_stats():
    display_lineup()
    try:
        index = int(input("Enter the player number to edit stats: ")) - 1
        if 0 <= index < len(lineup):
            while True:
                try:
                    at_bats = int(input("New at bats: "))
                    if at_bats >= 0:
                        break
                except ValueError:
                    pass
                print("Invalid entry. At bats must be a non-negative integer.")
            
            while True:
                try:
                    hits = int(input("New hits: "))
                    if 0 <= hits <= at_bats:
                        break
                except ValueError:
                    pass
                print("Invalid entry. Hits must be a non-negative integer and cannot exceed at bats.")
            
            lineup[index][2] = at_bats
            lineup[index][3] = hits
            print(f"{lineup[index][0]}'s stats were updated.")
        else:
            print("Invalid player number.")
    except ValueError:
        print("Invalid entry. Please enter a valid player number.")

def main():
    while True:
        display_menu()
        try:
            option = int(input("Menu option: "))
            if option == 1:
                display_lineup()
            elif option == 2:
                add_player()
            elif option == 3:
                remove_player()
            elif option == 4:
                move_player()
            elif option == 5:
                edit_player_position()
            elif option == 6:
                edit_player_stats()
            elif option == 7:
                print("Bye!")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Invalid entry. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
