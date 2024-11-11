import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import string


root = tk.Tk()
a = tk.IntVar()
s = tk.IntVar()


winsize=tk.IntVar()
winsize = "1000x800"
root.geometry(f"{winsize}")
root.title("Doom Text Editor")

root.resizable(False, False)

global mainfile
mainfile=""

fileContents = tk.StringVar()

def setText(word):
    fileContents.set(word)


# TEXT AREA

# input entry
editorbox = ScrolledText(root, height=600, width=800, fg='#ffffff', insertbackground='white', font=('Terminal', 14))
editorbox.pack()
editorbox['background'] = '#444444'

def SaveToFile1(filename):
    conten = editorbox.get("1.0",'end-1c')
    with open(f'{filename}', 'w') as usercont:
        usercont.write(conten)
        mainfile = filename
        print(mainfile)
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
            global mainfile
            mainfile = UserFileName
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
    global mainfile
    mainfile=filename


def savetofile():
    global mainfile
    if mainfile=="":
        SaveAs()
        return
    conten = editorbox.get("1.0",'end-1c')
    with open(f'{mainfile}', 'w') as usercont:
        usercont.write(conten)


def open_file():
    editorbox.delete("1.0",'end-1c')
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


    enterbutton = tk.Button(newWindow, text="Open", command=on_save)
    enterbutton.grid(column=1)



def save():
    savetofile()

def clear():
    global mainfile
    mainfile=""
    editorbox.delete("1.0",'end-1c')

def changesize():
    root.resizable(True, True)

# MENU


menu = tk.Menu(root, fg='#ffedff')
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=clear)
filemenu.add_command(label='Save', command=save)
filemenu.add_command(label='Save As...', command=SaveAs)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
viewmenu = tk.Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Resize', command=changesize)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Guide')
menu['background'] = '#656565'

root.mainloop()
