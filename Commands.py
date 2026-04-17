# TerminalOne
# Copyright (c) 2026 DashingA0pex
# Licensed under GPL 3.0
# See LICENSE file for details

#THIS is Commands.py, which contains all the commands for TerminalOne. This is imported into Home.py and used there.
from ast import arg
import os
from pydoc import text
import sys
import time
import Login
import platform
import pathlib
import Data_manager
import User_manager
import randfacts

# BASIC COMMANDS

def commands():
    """Show available commands"""
    print("Available commands:")
    print("")
    print("- commands: Show this help message")
    print("- clear: Clear the terminal screen")
    print("- logo(2-6): Show the TerminalOne logo in ASCII art")
    print("- styles: Show different color styles for TerminalOne")
    print("- logout: Exit TerminalOne and return to login")
    print("- sysinfo: Show system information (username, OS, Python version)")
    print("- whereami: Show current working directory")
    print("- viewfiles: Show files within the TerminalOne directory/folder")
    print("- say: Print text to the screen (like echo in Linux)")
    print("- whoami: Show the current logged-in user")
    print("===== FILE AND NOTE COMMANDS: =====")
    print('- savenote "note": Save a note to notes.json (e.g. savenote "This is a note")')
    print("- loadnote: Load and display all saved notes")
    print("- viewfiles: Show files in the data folder")
    print('- savemessage "message": Save a message to messages.json (e.g. savemessage "This is a message")')
    print("- loadmessage: Load and display all saved messages")

    print("===== TO BE ADDED: =====")
    print("- honesty: shows what's happening in the background of TerminalOne (for debugging)")

def say(*args):
    """Print text to the screen (echo equivalent)"""
    if args:
        text = " ".join(args)
        print(text)
    else:
        print("Usage: say <text>")


def whereami():
    """Show current working directory"""
    print("Current working directory: " + os.getcwd())

def clear():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def t_logout():
    """Logout and exit - renamed from exit() to avoid Python built-in"""
    print("Exiting TerminalOne...")
    time.sleep(1)
    sys.exit()

def sysinfo():
    print (r"===== System Information =====")
    print("Username: " + Login.Username)
    print("Current Working Directory:" + os.getcwd())
    print("Python Version: " + sys.version)
    print("Operating System: " + " " + platform.system())

def whoami():
    #Show current logged-in user
    current_user = Data_manager.get_current_user()
    if current_user:
        print(f"Current user: {current_user}")
    else:
        print("No user logged in.")


#   FILE COMMANDS

def viewfiles():
    """Show files in the data folder"""
    print("Files in data/:")
    try:
        for item in os.listdir('data'):
            if os.path.isfile(f'data/{item}'):
                print("- " + item)
    except FileNotFoundError:
        print("Data folder not found. Login first to create it.")

def savenote(*args):
    print("Enter your note (type 'END' on a new line when done):")
    note_lines = []
    while True:
        line = input("> ")
        if line == "END":
            break
        note_lines.append(line)
    
    note_text = "\n".join(note_lines)
    notes_data = Data_manager.load_json("notes.json")
    notes_data["notes"].append(note_text)
    Data_manager.save_json("notes.json", notes_data)
    print("Note saved!")

def loadnote(*args):

    import Data_manager
    notes_data = Data_manager.load_json("notes.json")
    if notes_data["notes"]:
        print("Your notes:")
        for i, note in enumerate(notes_data["notes"], 1):
            print(f"{i}. {note}")
    else:
        print("No notes saved yet.")

# OPEN FILE COMMANDS

def loadmessage(*args):
    messages_data = Data_manager.load_json("messages.json")
    if messages_data["messages"]:
        print("Your messages:")
        for i, message in enumerate(messages_data["messages"], 1):
            print(f"{i}. {message}")
    else:
        print("No messages saved yet.")

def openfile():
 #Opens and display a file from the data folder
    data_folder = "data"
    try:
        files = [f for f in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, f))]
        if not files:
            print("No files found in data/ folder.")
            return
        print("Files in data/: ")
        for i, f in enumerate(files, 1):
            print(f"{i}. {f}")
        filename = input("Enter the filename to open: ")
        filepath = os.path.join(data_folder, filename)
        if not os.path.isfile(filepath):
            print("File not found.")
            return
        with open(filepath, "r", encoding="utf-8") as file:
            print(f"\nContents of {filename}:\n")
            print(file.read())
    except FileNotFoundError:
        print("Data folder not found. Login first to create it.")


# LOGO COMMANDS

def logo():
    """Show ASCII logo 1"""
    print(r"""
   ______                     _             _ ____                
  /_  __/__  _________ ___  (_)___  ____ _/ / __ \____  ___      
   / / / _ \/ ___/ __ `__ \/ / __ \/ __ `/ / / / / __ \/ _ \     
  / / /  __/ /  / / / / / / / / / / /_/ / / /_/ / / / /  __/     
 /_/  \___/_/  /_/ /_/ /_/_/_/ /_/\__,_/_/\____/_/ /_/\___/      
""")


def logo2():
    """Show ASCII logo 2"""
    print(r"""
 ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗      ██████╗ ███╗   ██╗███████╗
 ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     ██╔═══██╗████╗  ██║██╔════╝
    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     ██║   ██║██╔██╗ ██║█████╗  
    ██║   ██╔════╝██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     ██║   ██║██║╚██╗██║██╔════╝
    ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗╚██████╔╝██║ ╚████║███████╗
    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
""")


def logo3():
    """Show ASCII logo 3"""
    print(r"""
  TerminalOne [Version 1.0]
  -------------------------
""")


def logo4():
    """Show ASCII logo 4"""
    print(r"""
  _____                   _             _ ____             
 |_   _|__ _ __ _ __ ___ (_)_ __   __ _| |  _ \ _ __   ___ 
   | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | | | '_ \ / _ \
   | |  __/ |  | | | | | | | | | | (_| | | |_| | | | |  __/
   |_|\___|_|  |_| |_| |_|_|_|_| |_|\__,_|_|____/|_| |_|\___|
""")


def logo5():
    """Show ASCII logo 5"""
    print(r"""
  _______                  _             _ ____               
 |__   __|                (_)           | |  _ \              
    | | ___ _ __ _ __ ___  _ _ __   __ _| | | | |_ __   ___  
    | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | | | '_ \ / _ \ 
    | |  __/ |  | | | | | | | | | | (_| | | |_| | | | |  __/ 
    |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|____/|_| |_|\___| 
""")


def logo6():
    """Show ASCII logo 6"""
    print(r"""
  ╔╦╗╔═╗╦═╗╔╦╗╦╔╗╔╔═╗╦  ╔═╗╔╗╔╔═╗
   ║ ║╣ ╠╦╝║║║║║║║╠═╣║  ║ ║║║║║╣ 
   ╩ ╚═╝╩╚═╩ ╩╩╝╚╝╩ ╩╩═╝╚═╝╝╚╝╚═╝
""")


# COLOR COMMANDS (Windows only)

def styles():
    """Show available color styles"""
    print("Available color styles:")
    print("- color_classic: White on black")
    print("- color2_matrix: Green on black (Matrix style)")
    print("- color3_ocean: Bright white on blue")
    print("- color4_sunset: Yellow on red")
    print("- color5_old: Bright white on yellow")
    print("\nNote: Color commands only work on Windows")


def color_classic():
    """White text on black background (Windows only)"""
    if os.name == 'nt':
        os.system('color 07')
    else:
        print("Color commands only work on Windows")


def color2_matrix():
    """Green text on black background (Windows only)"""
    if os.name == 'nt':
        os.system('color 0A')
    else:
        print("Color commands only work on Windows")


def color3_ocean():
    """Bright white on blue (Windows only)"""
    if os.name == 'nt':
        os.system('color 1F')
    else:
        print("Color commands only work on Windows")


def color4_sunset():
    """Yellow on red (Windows only)"""
    if os.name == 'nt':
        os.system('color 4E')
    else:
        print("Color commands only work on Windows")


def color5_old():
    """Bright white on yellow (Windows only)"""
    if os.name == 'nt':
        os.system('color 6F')
    else:
        print("Color commands only work on Windows")


#Fun stuff/Easter eggs

def funfact():
    fact = randfacts.get_fact()
    print(fact)
