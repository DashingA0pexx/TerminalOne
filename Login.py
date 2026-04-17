# TerminalOne
# Copyright (c) 2026 DashingA0pex
# Licensed under GPL 3.0
# See LICENSE file for details

import time
import sys
import os
import Data_manager

Username = "DashingA0pex"
Password = "Chezburger"


def perform_login():

    # Runs the login loop and return True if login successful, False if you're an invader that doesn't know the credentials!
    attempts = 0
    max_attempts = 3
    skip_login = "admin code 17g2j3: skip login"
    while attempts < max_attempts:
        print("\n" + "="*50)
        print("TerminalOne Login")
        print("="*50)
        print(f"Attempts remaining: {max_attempts - attempts}")
        
        print("Please enter your username:")
        user_input = input("> ").strip()
        
        # Checks if username is correct
        if user_input == Username:
            print("Username accepted. Please enter your password:")
            pass_input = input("> ")
            
            # Checks if password is correct
            if pass_input == Password:
                print("\nAccess granted. Welcome, " + Username + "!")
                Data_manager.initialize_default_files()  # ADD THIS
                time.sleep(1)
                print("Launching TerminalOne...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                return True
            
            else:
                print("Incorrect password. Try again.\n")
                attempts += 1
        else:
            print("Incorrect username. Try again.\n")
            attempts += 1
    
    # If we get here, max attempts exceeded soo it quits on it's own
    print("\nMax login attempts exceeded. Exiting...")
    time.sleep(2)
    return False