# TerminalOne

A lightweight terminal interface for managing local data and (eventually) communicating between devices.
Currently it's only supported on Windows but i'll add Linux support soon.

## About

TerminalOne is a CLI-based management layer that sits on top of operating systems. Currently in early development, it provides a clean interface for system commands, note-taking, and message storage – with plans to support distributed communication between devices (Desktop and Field editions).

Inspired by Armbian's simple, functional CLI design.
And on Github my username is actually "DashingA0pexx" with two X because if you look for DashingA0pex then it's my ghost account. The one I forgot my password for.

## Current Features

- Login System – Authentication
- Command Interface – Clean CLI for running commands
- Note Management – Save and load notes locally
- Message Storage – Store messages as JSON
- System Info – View OS, Python version, current directory
- File Management – View files in data folder
- ASCII Logos – Multiple terminal styling options

## Installation

1. Clone this repo
2. Install Python 3.12+
3. Run: `python TerminalOne.py`
4. Login with:
   - Username: `DashingA0pex`
   - Password: `Chezburger`

## Usage
```
savenote      # Save a multi-line note
loadnote      # Display all saved notes
savemessage   # Save a multi-line message
loadmessage   # Display all saved messages
commands      # View all available commands
clear         # Clear terminal screen
sysinfo       # Show system information
logout        # Exit TerminalOne
```

## Roadmap

- [x] Multi-user support
- [ ] Linux compatibility
- [ ] Field Edition (for SBCs)
- [ ] Networking between devices
- [ ] Real messaging system
- [ ] Desktop Edition with enhanced UI

## License

GPL 3.0 – See LICENSE file

## Contact

Found a bug? Have suggestions? Email: dashinga0pex.2026@gmail.com

(Note: I'm a student so responses may be slow, but I appreciate feedback!)