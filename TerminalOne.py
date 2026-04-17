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

# Main entry point for TerminalOne or THE LOGIN/SIGN-UP THINGGG
# -DashingA0pex
def main():
    # Main entry point for TerminalOne
    
    while True:

        print("\n" + "=" * 50)
        print("TerminalOne v1.0")
        print("=" * 50)
        print("Press Enter to login")
        print("Press 'q' to quit")

        # HERE is the choice. the > thing after an input like "> i <3 Linus Torvalds" basically the input thing in ALOT of CLIs
        user_choice = input("> ").strip().lower()
        os.system('cls' if os.name == 'nt' else 'clear')

        # Gets you to Login.py to begin the login sequence
        if user_choice == '' or user_choice == 'enter':
            if Login.perform_login():
                Home.run_home()
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nReturning to main menu...")
            else:
                print("Login failed. Try again.")

        # A special feature for me that I made because typing in my credentials abunch of times was annoying
        elif user_choice == 'debug':  # ADD THIS
            print("Skipping login...")
            Data_manager.initialize_default_files()  # ADD THIS
            Home.run_home()  # ADD THIS
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