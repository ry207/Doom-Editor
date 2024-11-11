import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import string



root = tk.Tk()
a = tk.IntVar()
root.geometry("1000x800")
root.title("Doom")
root.resizable(False, False)


fileContents = tk.StringVar()

def setText(word):
    fileContents.set(word)


# TEXT AREA

# input entry
editorbox = ScrolledText(root, height=600, width=800)
editorbox.pack()

def SaveToFile1(filename):
    conten = editorbox.get("1.0",'end-1c')
    with open(f'{filename}', 'w') as usercont:
        usercont.write(conten)

    return

def SaveAs():
    newWindow = tk.Toplevel(root)
    newWindow.title("Save As...")
    newWindow.geometry("400x200")

    filelabel = tk.Label(newWindow, text="Enter file name: ", font=('Arial', 14))
    filelabel.grid(row=1, column=0)

    filename = tk.Entry(newWindow, width=20, font=('Arial', 12))
    filename.grid(row=2, column=1, pady=2)

    # Define the button to trigger the save operation
    def on_save():
        UserFileName = filename.get()
        if UserFileName:  # Only proceed if the user entered a filename
            SaveToFile1(UserFileName)
            newWindow.destroy()  # Optionally close the "Save As" window after saving
        else:
            print("No filename entered.")

    enterbutton = tk.Button(newWindow, text="Save", command=on_save)
    enterbutton.grid(column=1)


def OpenFile1(filename):
    # The file saving logic will now be inside this function

    with open(f'{filename}', 'r') as filecont:
        fileContents = filecont.read()
        editorbox.insert(tk.INSERT,fileContents)


def open_file():
    newWindow = tk.Toplevel(root)
    newWindow.title("Open")
    newWindow.geometry("400x200")

    filelabel = tk.Label(newWindow, text="Enter file name: ", font=('Arial', 14))
    filelabel.grid(row=1, column=0)

    filename = tk.Entry(newWindow, width=20, font=('Arial', 12))
    filename.grid(row=2, column=1, pady=2)

    # Define the button to trigger the save operation
    def on_save():
        UserFileName = filename.get()
        if UserFileName:  # Only proceed if the user entered a filename
            OpenFile1(UserFileName)
            newWindow.destroy()  # Optionally close the "Save As" window after saving
        else:
            print("No filename entered.")

    enterbutton = tk.Button(newWindow, text="Save", command=on_save)
    enterbutton.grid(column=1)



# MENU

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Save', command=SaveAs)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_separator()
filemenu.add_command(label='Exit')
viewmenu = tk.Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Size')
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Guide')

root.mainloop()
