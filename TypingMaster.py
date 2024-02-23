import random #FOR CHOOSING RANDOM WORDS
import time # TO CALCULATE REAL TIME 
import json #TO USE JSON OBJECTS

import os
os.system("color")
from termcolor import colored #TO GIVE TERMINAL COLOR

def UpdateLeaderBoard(username,wpm):
    

    try: #TO PREVENT FROM ERROR
        with open("LeaderBoard.json","r") as f: #KISI BHI FILE KO APNI MAIN FILE ME OPEN KRNA
            leaderboard = json.load(f) # JSON OBJECT TO PYTHON DICT

    except FileNotFoundError: #To handle the Error of empty file
        leaderboard = {} 
    
    
    leaderboard[username] = wpm #UPDATE THE DATA OF USER
    
    #sort  (SORTED ==> LIST)
    leaderboard = dict(sorted(leaderboard.items(),key = lambda item:item[1] ,reverse=True) )
   
    #python-dict ==>json
    with open ("LeaderBoard.json","w") as g: #R ==> READ , "W"==>"wRITE"
        json.dump(leaderboard,g) #DUMP ==> DICT TO JSON OBJECT

def ShowLeaderBoard():
    with open ("LeaderBoard.json","r") as file :
        leaderboard=json.load (file)
    return leaderboard #leaderboard ek dictionary hai

def main():

    print()
    print(colored("Welcome to Terminal Typing Master!⌨️","red","on_white"))
    print()
    username = input("\nEnter your username :- ")

    while True:
        print("\nOptions:\n")
        print("1. Start Typing Test ⌨️")
        print("2. Show Leaderboard")
        print("3. Exit ❌")
        choice = input("\nEnter your choice :- ")

        if choice == "1":
            category = input("\nChoose a category (e.g., animals, fruits): ")
            print()
            words = load_words_from_category(category) #ARRAY MILEGI JISME KUCH WORDS(5)
            start_time = time.time() #JAB USER START KREGA TB TIME STORE KR LEGA
            words_typed = 0
            ACCURATE_WORD = 0
            for word in words: #EK EK KARKE SB WORDS DEGA
                print(word) 
                user_input = input("\nType the word (Ctrl + Q to quit ❌): ")
                print()
                if user_input.lower() == "ctrl+q":
                    print("Exiting❌ Typing Test...")
                    break

                if user_input == word:
                    ACCURATE_WORD+=1
                words_typed += 1
            print("ACCURACTE_WORDS",ACCURATE_WORD)

            end_time = time.time() #end time
            time_taken = end_time - start_time
            wpm = calculate_wpm(words_typed, time_taken,ACCURATE_WORD) 
            print(f"\nWords Per Minute (WPM): {wpm:.2f}") #f' string
            
            UpdateLeaderBoard(username,wpm) #username aur wpm ko leaderboard updae krenge
            
        elif choice=="2":
            # UpdateLeaderBoard(username,wpm)
            my_leaderboard = ShowLeaderBoard() #ek dictionary milegi jisme realtime data

            print()
            print(colored("LeaderBoard :- ","green"))
            print()

            # print(my_leaderboard)
            rank = 1
            for j in my_leaderboard:
                
                print(f"{rank}.  {j} ->  {my_leaderboard[j]:.2f} WPM")
                rank+=1
            
        elif choice == "3":
            print()
            print(colored("Exiting❌ Terminal Typing Master⌨️...","black","on_white"))
            print()
            break

        else:
            print()
            print(colored("Invalid choice!!❎","black","on_light_red"))
            print()
            print("Please choose again.")
            print()

def load_words_from_category(category):
    if category == "animals":
        return ["cat", "dog", "elephant", "lion", "tiger"]
    elif category == "fruits":
        return ["apple", "banana", "orange", "grape", "watermelon"]
    else:
        print("Invalid category. Using default category 'animals'.")
        return ["cat", "dog", "elephant", "lion", "tiger"]

def calculate_wpm(words_typed, time_taken,correct_word):
    wpm = (correct_word / 5) / (time_taken / 60)  # Assuming 5 words per sentence
    return wpm

if __name__ == "__main__":
    main()