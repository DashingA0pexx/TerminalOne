# TerminalOne
# Copyright (c) 2026 DashingA0pex
# Licensed under GPL 3.0
# See LICENSE file for details

import os
import sys
import time
import Login
import Commands
import Data_manager


def run_home(username):
    """Run the home screen for the logged-in user"""
    print(
        ''' 
TerminalOne
Copyright (c) 2026 DashingA0pex
Licensed under GPL 3.0
See LICENSE file for details
        '''
    )
    time.sleep(1)
    print(r"""
   ______                    _            _ ____                
  /_  __/__  _________ ___  (_)___  ____ _/ / __ \____  ___      
   / / / _ \/ ___/ __ `__ \/ / __ \/ __ `/ / / / / __ \/ _ \     
  / / /  __/ /  / / / / / / / / / / /_/ / / /_/ / / / /  __/     
 /_/  \___/_/  /_/ /_/ /_/_/_/ /_/\__,_/_/\____/_/ /_/\___/      
""")
    print(f"\nWelcome to the Home Screen, {username}!")
    print("This is where you can access your terminal commands and features.")
    time.sleep(0.5)
    print('Type "commands" for a list of available commands, or "logout" to exit.')
    
    # Initialize default files for this user on first run
    Data_manager.initialize_default_files()
    
    while True:
        line = input(username + "@TerminalOne $> ").strip()
        
        # Ignore blank lines
        if not line:
            continue
        
        # Split command and arguments
        parts = line.split()
        cmd = parts[0].lower()
        args = parts[1:]
        
        # Handle logout specially
        if cmd == "logout":
            print("Logging out...")
            time.sleep(1)
            return  # Exit the function, go back to main menu
        
        # Try to call the command from Commands module
        if hasattr(Commands, cmd):
            try:
                getattr(Commands, cmd)(*args)
            except Exception as e:
                print(f"Error executing command: {e}")
        else:
            print(f"{cmd}: Command not found. Type 'commands' for help.")