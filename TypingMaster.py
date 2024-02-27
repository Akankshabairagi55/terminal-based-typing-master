import random # Importing the random module to choose random words
import time # Importing the time module to calculate real-time duration
import json # Importing the json module to work with JSON objects

import os
os.system("color") # Setting color settings for the terminal
from termcolor import colored # Importing colored function to add color to terminal text

def UpdateLeaderBoard(username,wpm):
    try: # Try block to prevent errors
        with open("LeaderBoard.json","r") as f: # Opening a file to read JSON data
            leaderboard = json.load(f) # Loading JSON data into a Python dictionary
    except FileNotFoundError: # Handling the error if the file doesn't exist
        leaderboard = {} # If file doesn't exist, initialize an empty dictionary
    
    leaderboard[username] = wpm # Update the dictionary with the username and WPM
    
    # Sort the leaderboard based on WPM in descending order
    leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))
    
    # Writing the updated leaderboard dictionary back to the JSON file
    with open("LeaderBoard.json", "w") as g: # Opening the file to write JSON data
        json.dump(leaderboard, g) # Dumping the dictionary data back to the file

def ShowLeaderBoard():
    with open("LeaderBoard.json", "r") as file: # Opening the JSON file to read data
        leaderboard = json.load(file) # Loading JSON data into a Python dictionary
    return leaderboard # Return the leaderboard dictionary

def main():
    print()
    print(colored("Welcome to Terminal Typing Master!⌨️", "red", "on_white")) # Displaying welcome message
    print()
    username = input("\nEnter your username :- ") # Taking user input for username

    while True: # Start of the main game loop
        print("\nOptions:\n") # Displaying available options to the user
        print("1. Start Typing Test ⌨️")
        print("2. Show Leaderboard")
        print("3. Exit ❌")
        choice = input("\nEnter your choice :- ") # Taking user input for their choice
        
        if choice == "1": # If the user chooses to start the typing test
            category = input("\nChoose a category (e.g., animals, fruits): ") # Taking user input for category
            print()
            words = load_words_from_category(category) # Loading words based on chosen category
            start_time = time.time() # Start time of the typing test
            words_typed = 0 # Initialize variable to count the number of words typed
            correct_words = 0 # Initialize variable to count the number of correct words typed
            for word in words: # Loop through each word in the list of words
                print(word) # Display the word to be typed
                user_input = input("\nType the word (Ctrl + Q to quit ❌): ") # Prompt the user to type the word
                print()
                if user_input.lower() == "ctrl+q": # If user wants to quit
                    print("Exiting❌ Typing Test...") # Display exit message
                    break # Break out of the loop
                
                if user_input == word: # If the typed word matches the word to be typed
                    correct_words += 1 # Increment the count of correct words
                words_typed += 1 # Increment the count of total words typed
            print("CORRECT WORDS:", correct_words) # Display the number of correct words typed

            end_time = time.time() # End time of the typing test
            time_taken = end_time - start_time # Calculate the duration of the typing test
            wpm = calculate_wpm(words_typed, time_taken, correct_words) # Calculate WPM
            print(f"\nWords Per Minute (WPM): {wpm:.2f}") # Display the calculated WPM
            
            UpdateLeaderBoard(username, wpm) # Update the leaderboard with the username and WPM
        
        elif choice == "2": # If the user chooses to show the leaderboard
            my_leaderboard = ShowLeaderBoard() # Get the leaderboard data
            print()
            print(colored("Leaderboard :- ", "green")) # Display leaderboard heading
            print()
            rank = 1 # Initialize rank counter
            for j in my_leaderboard: # Loop through each entry in the leaderboard
                print(f"{rank}.  {j} ->  {my_leaderboard[j]:.2f} WPM") # Display username and WPM
                rank += 1 # Increment rank counter
        
        elif choice == "3": # If the user chooses to exit the game
            print()
            print(colored("Exiting❌ Terminal Typing Master⌨️...", "black", "on_white")) # Display exit message
            print()
            break 