import tkinter as tk
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import os
import subprocess


# STARTING INFO

root = tk.Tk()
a = tk.IntVar()
s = tk.IntVar()
global font
font = 12

winsize = tk.IntVar()
winsize = "900x600"
root.geometry(f"{winsize}")
root.title("Doom Text Editor")

global fgc
global bgc
global ibc
fgc = "#ffb7c5"
bgc = "#252525"
ibc = "#ffffff"

root.resizable(True, True)

global mainfile
mainfile = ""

fileContents = tk.StringVar()

def setText(word):
    fileContents.set(word)

# TEXT AREA

editorbox = ScrolledText(root, height=600, width=800,
                         fg=f'{fgc}',               # Soft Mint Green for text
                         insertbackground=f'{ibc}',  # Light Gray cursor color
                         font=("Courier New", f"{font}", "bold"),
                         undo=True)
editorbox.config(borderwidth=3, relief='ridge')  # Adds a 3-pixel border around the text area
editorbox.pack()
editorbox['background'] = f'{bgc}'


# Doom Command Console Window
def show_command_prompt():
    cmd_window = tk.Toplevel(root)
    cmd_window.title("Doom Command Prompt")
    cmd_window.geometry("600x300")

    cmd_window.resizable(False, False)  # Make the command prompt window non-resizable

    # Set background color for the command prompt window
    cmd_window.configure(bg=f'{bgc}')

    # Command prompt label
    label = tk.Label(cmd_window, text="Enter Command (clear, save, exit, explorer, help, color):", font=("Courier New", 12), fg=f"{fgc}", bg=f"{bgc}")
    label.pack(pady=10)

    # Command entry box with a darker background than the main window
    command_entry = tk.Entry(cmd_window, width=50, font=("Courier New", 12), fg=f"{fgc}", bg=f"{bgc}", insertbackground=f"{ibc}", relief="flat")
    command_entry.pack(pady=10)

    # Console output (Text widget to display command results) with a matching dark background
    console_output = ScrolledText(cmd_window, width=70, height=10, font=("Courier New", 10), fg=f"{fgc}", bg=f"{bgc}", insertbackground=f"{ibc}", relief="flat")
    console_output.pack(pady=10)

    # Function to process command when Enter key is pressed
    def process_command(event=None):
        command = command_entry.get()
        command_entry.delete(0, tk.END)  # Clear the entry box

        # Command processing logic
        if command.lower() == "clear":
            editorbox.delete(1.0, tk.END)
            global mainfile
            mainfile=""
            append_to_console("Editor cleared.\n")
        elif command.lower() == "save":
            if mainfile == "":
                append_to_console("No file to save. Please use 'save as' to specify a file.\n")
            else:
                savetofile()
                append_to_console(f"File saved as {mainfile}\n")
        elif command.lower() == "save as":
            append_to_console("Save as...\n")
            SaveAs()
        elif command.lower() == "exit":
            append_to_console("K bye\n")
            root.quit()  # Quit the application
        elif command.lower() == "color":
            append_to_console("Color Properties...\n")
            colorprop()  # 
        elif command.lower() == "explorer":
            append_to_console("Opening file explorer\n")
            open_file_explorer()
        elif command.lower() == "help":
            append_to_console("Opening help menu...!\n")
            show_guide()
        else:
            append_to_console(f"Unknown command: {command}\n")

    command_entry.bind("<Return>", process_command)  # Bind Enter key to process the command

    # Function to append output to the console in the command prompt
    def append_to_console(text):
        console_output.insert(tk.END, text + "\n")
        console_output.yview(tk.END)  # Scroll to the bottom

# Save File
def SaveToFile1(filename):
    conten = editorbox.get("1.0", 'end-1c')
    with open(f'{filename}', 'w') as usercont:
        usercont.write(conten)
        global mainfile
        mainfile = filename
    return

def SaveAs():
    # Open the file dialog to choose the location and name of the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("All files", "*.*")],
                                             title="Save As")

    # Check if the user selected a file path (it should not be empty)
    if file_path:
        global mainfile
        mainfile = file_path
        SaveToFile1(file_path)  # Save the content to the selected file path
    else:
        print("Save operation was canceled.")

def savetofile():
    global mainfile
    if mainfile == "":
        SaveAs()
        return
    conten = editorbox.get("1.0", 'end-1c')
    with open(f'{mainfile}', 'w') as usercont:
        usercont.write(conten)

# Open File
def OpenFile1(filename):
    with open(f'{filename}', 'r') as filecont:
        fileContents = filecont.read()
        editorbox.insert(tk.INSERT, fileContents)
    global mainfile
    mainfile = filename


def open_file(filename):
    editorbox.delete("1.0", 'end-1c')
    OpenFile1(filename)


# Random Functions
def clear():
    global mainfile
    mainfile = ""
    editorbox.delete("1.0", "end-1c")

def insert_tab(event):
    editorbox.insert(tk.INSERT, " " * 4)  # Insert 4 spaces
    return "break"  # Prevent the default tab behavior

# Open File Explorer
def open_file_explorer():
    # This will open the file explorer using the default file dialog
    filename = filedialog.askopenfilename()  # Prompt to choose a file
    if filename:
        open_file(filename)  # If a file is selected, open it


def undo_action(event=None):
    try:
        editorbox.edit_undo()  # Calls the undo operation on the editor
    except tk.TclError:
        pass  # If there's nothing to undo, do nothing

def select_all(event=None):
    editorbox.tag_add('sel', '1.0', 'end')
    return "break"


# Change color window
def colorprop():
    colorwindow = tk.Toplevel(root)
    colorwindow.title("Color properties")
    colorwindow.geometry("800x400")
    colorwindow.resizable(True, True)

    # Set background color for the guide window
    colorwindow.configure(bg=f'{bgc}')

    tk.Label(colorwindow, font=("Courier New", 14), text="", bg=f"{bgc}", fg=f"{fgc}", width=400).pack=()

    colorbgclabel = tk.Label(colorwindow, text="Background Color:", bg=f"{bgc}", fg=f"{fgc}")
    colorbgclabel.pack()
    colorbgc = tk.Entry(colorwindow, width=50, font=("Courier New", 12), fg=f"{fgc}", bg=f"{bgc}", insertbackground=f"{ibc}", relief="flat")
    colorbgc.pack()

    colorfgclabel = tk.Label(colorwindow, text="Text Color:", bg=f"{bgc}", fg=f"{fgc}")
    colorfgclabel.pack()
    colorfgc = tk.Entry(colorwindow, width=50, font=("Courier New", 12), fg=f"{fgc}", bg=f"{bgc}", insertbackground=f"{ibc}", relief="flat")
    colorfgc.pack()

    coloribclabel = tk.Label(colorwindow, text="Cursor Color:", bg=f"{bgc}", fg=f"{fgc}")
    coloribclabel.pack()
    coloribc = tk.Entry(colorwindow, width=50, font=("Courier New", 12), fg=f"{fgc}", bg=f"{bgc}", insertbackground=f"{ibc}", relief="flat")
    coloribc.pack()

    def change_font():
        value = spinbox.get()
        global font
        font = value
        editorbox.config(font=("Courier New", f"{font}", "bold"))

        spinbox.bind("<Return>", lambda event: change_font())

    spinbox = tk.Spinbox(colorwindow, from_=9, to=42, width=10, relief="sunken", repeatdelay=500, repeatinterval=100,
                     font=("Arial", 12), bg=f"{bgc}", fg=f"{fgc}", command=change_font, highlightbackground = "black", highlightcolor= "black")
    spinbox.config(state="normal", cursor="hand2", bd=3, justify="center", wrap=True)
    spinbox.pack(padx=20, pady=20)

    def update():
        global bgc
        global fgc
        global ibc
        if (colorbgc.get() == ""):
            bgc = bgc
        elif (colorbgc.get() == "reset"):
            bgc = "#2B3E42"
        else:
            bgc = colorbgc.get()
        if (colorfgc.get() == ""):
            fgc = fgc
        elif (colorfgc.get() == "reset"):
            fgc = "#C3E88D"
        else:
            fgc = colorfgc.get()
        if (coloribc.get() == ""):
            ibc = ibc
        elif (coloribc.get() == "reset"):
            ibc = "#A9A9A9"
        else:
            ibc = coloribc.get()
        editorbox.config(borderwidth=3, relief='ridge', fg=f"{fgc}", bg=f"{bgc}", insertbackground=f"{ibc}") 

    enter_button = tk.Button(colorwindow, text="Enter", command=update, bg=f"{bgc}", fg=f"{fgc}")
    enter_button.pack()



# Guide
def show_guide():
    guideWindow = tk.Toplevel(root)
    guideWindow.title("Guide")
    guideWindow.geometry("600x800")
    guideWindow.resizable(True, True)

    # Set background color for the guide window
    guideWindow.configure(bg=f'{bgc}')

    guide_text = """Welcome to Doom Text Editor!

Here's a quick guide on how to use the main features:

- New: Clears the current text and starts a new document.
- Save: Saves the current document to the last saved location.
 - Save As: Allows you to save the document under a new filename.
- Open: Opens a file, replacing any existing text in the editor.
- Resize: Enables the window to be resizable.
- Properties: Change the properties of the editor including; background color, text color, text size and cursor color

Keyboard Shortcuts:
- Ctrl+S: Quick save.
- Ctrl+O: Open file.
- Ctrl+N: Start new document.
- Ctrl+Z: Undo
- Ctrl+G: Guide
- Alt+P: Properties
- Alt+E: Exit

Properties:
- Enter hex codes for any of the listed elements then press enter, type "reset" in the wanted field to reset the element to default.
- Change the font size with the spin box.
    -Either type and press return or use the arrows.

Command Prompt Features:
- Enter the command "clear" to clear the text editor.
- Enter the command "save" to save the document.
- Enter the command "explorer " to open the file explorer where you can select a file to edit.
- Enter "exit" to quit the editor.
- Enter "help" to open the guide.
- Enter "properties" to open the properties.

Enjoy writing with Doom Text Editor!"""

    # Apply the same styling to the guide label as the rest of the app
    guide_label = tk.Label(guideWindow, text=guide_text, font=('Courier New', 12), fg=f'{fgc}', bg=f'{bgc}', justify="left", wraplength=450)
    guide_label.pack(pady=10, padx=10)

# MENU

root.bind('<Control-s>', lambda event: savetofile())  # Ctrl+S to save
root.bind('<Control-n>', lambda event: clear())       # Ctrl+N for new document
root.bind('<Control-o>', lambda event: open_file_explorer())  # Ctrl+O to open file
root.bind('<Control-z>', undo_action)
root.bind('<Control-g>', lambda event: show_guide())
root.bind('<Control-Key-a>', select_all)
root.bind('<Alt-e>', lambda event: root.quit())
root.bind('<Alt-p>', lambda event: colorprop())
editorbox.bind("<Tab>", insert_tab)                   # Tab prints 4 spaces instead of 8

menu = tk.Menu(root, fg='#ffedff')
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=clear)
filemenu.add_command(label='Save', command=savetofile)
filemenu.add_command(label='Save As...', command=SaveAs)
filemenu.add_command(label='Open', command=open_file_explorer)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
viewmenu = tk.Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Command Prompt', command=show_command_prompt)
viewmenu.add_command(label='Properties', command=colorprop)

helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Guide', command=show_guide)

menu['background'] = '#656565'


root.mainloop()

    
