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
import User_manager

# Track current logged-in user
current_user = None

def set_current_user(username):
    """Set the currently logged-in user"""
    global current_user
    current_user = username

def get_current_user():
    """Get the currently logged-in user"""
    return current_user

#To make the User's data folder where the user's stuff like files, notes, etc will be stored.
#This is for when a user logs in for the first time, it will create a folder for them to store their data in.
#And other than making a new folder, it will also manage user data and maybe system data 

def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data", exist_ok=True)

def load_json(filename):
    """Load JSON file from current user's folder"""
    if current_user is None:
        raise RuntimeError("No user logged in!")
    
    user_path = User_manager.get_user_data_path(current_user)
    filepath = f"{user_path}/{filename}"
    
    with open(filepath, "r") as file:
        data = json.load(file)
    return data

def save_json(filename, data):
    """Save JSON file to current user's folder"""
    if current_user is None:
        raise RuntimeError("No user logged in!")
    
    user_path = User_manager.get_user_data_path(current_user)
    filepath = f"{user_path}/{filename}"
    
    with open(filepath, "w") as file:
        json.dump(data, file)

def initialize_default_files():
    """Create default JSON files for current user if they don't exist"""
    create_data_folder()
    
    if current_user is None:
        raise RuntimeError("No user logged in!")
    
    user_path = User_manager.get_user_data_path(current_user)
    
    default_files = {
        "messages.json": {"messages": []},
        "notes.json": {"notes": []},
        "settings.json": {"theme": "classic", "username": current_user}
    }
    
    for filename, default_data in default_files.items():
        filepath = f"{user_path}/{filename}"
        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                json.dump(default_data, file)