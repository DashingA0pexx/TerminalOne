# TerminalOne
# Copyright (c) 2026 DashingA0pex
# Licensed under GPL 3.0
# See LICENSE file for details


# THE DATA MANAGERRR! Used to manage data and system data within TerminalOne or other stuff idk bcs in the time I made
# this comment i'm still developing TerminalOne and it's stuff soo there might be new stuff to come soon
# -DashingA0pex 
import os
import sys
import json
import pathlib
import shutil

#To make the User's data folder where the user's stuff like files, notes, etc will be stored.
#This is for when a user logs in for the first time, it will create a folder for them to store their data in.
#And other than making a new folder, it will also manage user data and maybe system data 

def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data", exist_ok=True)
        print("Data folder created successfully.")
    else:
        print("Data folder already exists.")

def load_json(filename):
    with open(f"data/{filename}", "r") as file:
        data = json.load(file)
    return data

def save_json(filename, data):
    with open(f"data/{filename}", "w") as file:
        json.dump(data, file)

def initialize_default_files():
    """Create default JSON files if they don't exist"""
    create_data_folder()
    
    default_files = {
        "messages.json": {"messages": []},
        "notes.json": {"notes": []},
        "settings.json": {"theme": "classic", "username": "DashingA0pex"}
    }
    
    for filename, default_data in default_files.items():
        if not os.path.exists(f"data/{filename}"):
            save_json(filename, default_data)
            print(f"{filename} created with defaults.")