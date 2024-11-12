Doom Text Editor

Doom Text Editor is an advanced text editor with a dark, "Doom-inspired" aesthetic and command-line prompt for custom commands. This editor is perfect for developers and writers who enjoy a sleek, focused interface with advanced features.

Features

    Resizable editor with custom themes
    Command Prompt: Execute commands like save, open <filename>, clear, and exit directly from the command console
    Basic file operations: New, Save, Save As, Open
    Shortcut Keys:
        Ctrl+S: Quick save
        Ctrl+O: Open file
        Ctrl+N: New document

Guide

For a complete guide on how to use the editor and console commands, go to the Help > Guide section within the editor.
Command Prompt Features:

In the command prompt, you can type the following commands:

    clear: Clears the editor content
    save: Saves the document (if previously saved)
    open <filename>: Opens a specified file
    exit: Closes the editor
    open with explorer: Opens the file explorer to locate and open files

Installation and Usage
1. Prerequisites

    Python: Version 3.8 or higher. You can download it from python.org.
    Tkinter: This should come bundled with Python. Install it separately if needed:

    # Debian/Ubuntu
    sudo apt-get install python3-tk
    # macOS (usually pre-installed)
    brew install python-tk

2. Running Locally

Clone the repository and navigate to the project directory:

git clone https://github.com/yourusername/DoomTextEditor.git
cd DoomTextEditor
python3 main.py

3. Building an Executable

To create standalone executables on Windows, macOS, and Linux, follow these steps.
Install PyInstaller

PyInstaller is used to bundle the application:

pip install pyinstaller

Build Instructions

    Windows:

pyinstaller --onefile --windowed main.py

This creates an executable in the dist folder. The --windowed option hides the console window.

macOS:

pyinstaller --onefile --windowed main.py

PyInstaller will create a dist folder with a standalone .app file. You may need to adjust the security settings on macOS to open the app.

Linux:

    pyinstaller --onefile main.py

    This will create an executable in the dist folder, which you can run by typing ./DoomTextEditor.

4. Creating a Desktop Shortcut (Linux)

To create a desktop shortcut, create a .desktop file in ~/.local/share/applications/:

[Desktop Entry]
Name=Doom Text Editor
Comment=Advanced Text Editor with Doom Vibes
Exec=/home/yourusername/DoomTextEditor/dist/DoomTextEditor
Icon=/home/yourusername/DoomTextEditor/icon.png
Terminal=false
Type=Application
Categories=Utility;TextEditor;

Replace /home/yourusername/DoomTextEditor/dist/DoomTextEditor with the path to your executable and /home/yourusername/DoomTextEditor/icon.png with the path to an icon file.
Contributing

Feel free to submit pull requests, suggest new features, or report issues in the Issues section.
License

This project is licensed under the MIT License. See LICENSE for more information.
