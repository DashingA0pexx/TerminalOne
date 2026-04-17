# TerminalOne
# Copyright (c) 2026 DashingA0pex
# Licensed under GPL 3.0
# See LICENSE file for details

import os
import json

USERS_FILE = "data/users.json"

def load_users():
    """Load all users from users.json"""
    if not os.path.exists(USERS_FILE):
        return {}
    
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # If file is corrupted, return empty
        return {}

def save_users(users):
    """Save users to users.json"""
    os.makedirs("data", exist_ok=True)
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=2)

def user_exists(username):
    """Check if a user already exists"""
    users = load_users()
    return username in users

def create_user(username, password):
    """Create a new user account"""
    if user_exists(username):
        return False, f"User '{username}' already exists!"
    
    users = load_users()
    users[username] = password
    save_users(users)
    
    # Create user's data folder
    user_folder = get_user_data_path(username)
    os.makedirs(user_folder, exist_ok=True)
    
    # Initialize user's default files
    _initialize_user_files(username)
    
    return True, f"User '{username}' created successfully!"

def verify_user(username, password):
    """Check if username/password combination is correct"""
    users = load_users()
    
    if username not in users:
        return False
    
    if users[username] == password:
        return True
    else:
        return False

def get_user_data_path(username):
    """Return the data folder path for a specific user"""
    return f"data/{username}"

def _initialize_user_files(username):
    """Initialize default JSON files for a new user"""
    user_path = get_user_data_path(username)
    
    default_files = {
        "messages.json": {"messages": []},
        "notes.json": {"notes": []},
        "settings.json": {"theme": "classic", "username": username}
    }
    
    for filename, default_data in default_files.items():
        filepath = f"{user_path}/{filename}"
        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                json.dump(default_data, file)
