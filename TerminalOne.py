# TerminalOne
# Copyright (c) 2026 DashingA0pex
# Licensed under GPL 3.0
# See LICENSE file for details

import time
import sys
import Login
import Home
import os
import keyboard 
import Data_manager
import User_manager

# Main entry point for TerminalOne or THE LOGIN/SIGN-UP THINGGG
# -DashingA0pex
def main():
    # Main entry point for TerminalOne
    
    while True:

        print("\n" + "=" * 50)
        print("TerminalOne v1.0")
        print("=" * 50)
        print("Press Enter to login")
        print("Press 'r' to register")
        print("Press 'q' to quit")

        # HERE is the choice. the > thing after an input like "> i <3 Linus Torvalds" basically the input thing in ALOT of CLIs
        user_choice = input("> ").strip().lower()
        os.system('cls' if os.name == 'nt' else 'clear')

        # Gets you to Login.py to begin the login sequence
        if user_choice == '' or user_choice == 'enter':
            username = Login.perform_login()
            if username:
                Home.run_home(username)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nReturning to main menu...")
            else:
                print("Login failed. Try again.")
        
        # New registration option
        elif user_choice == 'r':
            if Login.perform_registration():
                print("Registration successful! You can now login.")
                time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        # A special feature for me that I made because typing in my credentials abunch of times was annoying
        elif user_choice == 'debug':  # ADD THIS
            print("Skipping login...")
            Data_manager.set_current_user("DashingA0pex")
            Home.run_home("DashingA0pex")  # ADD THIS
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nReturning to main menu...")

        # Orr if you changed your mind and that you decide to quit the program
        elif user_choice == 'q':
            print("Exiting TerminalOne...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()