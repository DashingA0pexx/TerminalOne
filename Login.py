# TerminalOne
# Copyright (c) 2026 DashingA0pex
# Licensed under GPL 3.0
# See LICENSE file for details

import time
import sys
import os
import Data_manager
import User_manager

# Legacy fallback (for backward compatibility)
Username = "DashingA0pex"
Password = "Chezburger"


def perform_login():
    """Multi-user login - returns username if successful, None otherwise"""
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\n" + "="*50)
        print("TerminalOne Login")
        print("="*50)
        print(f"Attempts remaining: {max_attempts - attempts}")
        
        print("Username:")
        username = input("> ").strip()
        
        print("Password:")
        password = input("> ")
        
        # Verify using User_manager
        if User_manager.verify_user(username, password):
            print(f"\nAccess granted. Welcome, {username}!")
            Data_manager.set_current_user(username)
            time.sleep(1)
            print("Launching TerminalOne...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return username  # Return username instead of True
        else:
            print("Incorrect credentials. Try again.\n")
            attempts += 1
    
    print("\nMax login attempts exceeded. Exiting...")
    time.sleep(2)
    return None


def perform_registration():
    """Register a new user account"""
    print("\n" + "="*50)
    print("TerminalOne Registration")
    print("="*50)
    
    username = input("Enter username: ").strip()
    
    if username == "":
        print("Username cannot be empty!")
        return False
    
    if User_manager.user_exists(username):
        print(f"Username '{username}' already taken!")
        return False
    
    password = input("Enter password: ")
    confirm = input("Confirm password: ")
    
    if password != confirm:
        print("Passwords don't match!")
        return False
    
    if password == "":
        print("Password cannot be empty!")
        return False
    
    success, message = User_manager.create_user(username, password)
    print(message)
    return success