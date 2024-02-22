import random
import time
import json

import os
os.system("color")
from termcolor import colored

def main():
    # UpdateLeaderBoard
    print(colored("\nWelcome to Terminal Typing Master!⌨️","black","on_white"))
    username = input("\nEnter your username : ")

    while True:
        print("\nOptions:")
        print("1. Start Typing Test ⌨️")
        print("2. Show Leaderboard")
        print("3. Exit ❌")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Choose a category (e.g., animals, fruits): ")
            words = load_words_from_category(category)
            start_time = time.time()
            words_typed = 0

            for word in words:
                print(word)
                user_input = input("Type the word (Ctrl + Q to quit ❌): ")
                if user_input.lower() == "ctrl+q":
                    print("Exiting Typing Test...")
                    break
                words_typed += 1

            end_time = time.time()
            time_taken = end_time - start_time
            wpm = calculate_wpm(words_typed, time_taken)
            print(f"\nWords Per Minute (WPM): {wpm:.2f}")
            
            UpdateLeaderBoard(username,wpm)
            
        elif choice=="2":
            # UpdateLeaderBoard(username,wpm)
            my_leaderboard = ShowLeaderBoard()
            # print(my_leaderboard)
            rank = 1
            for j in my_leaderboard:
                
                print(str(rank)+".    "+j+"     - "+str(my_leaderboard[j]))
                rank+=1
            
        elif choice == "3":
            print("Exiting Terminal Typing Master⌨️...")
            break

        else:
            print("Invalid❎choice!! Please choose again.")

if __name__ == "__main__":
    main()