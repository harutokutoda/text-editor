from tkinter import *
from tkinter.messagebox import *

def about():
    showinfo("About", "Text Editor\nVersion 1.0\n\nA simple text editor built with Python and Tkinter.")

def main(root, text, menubar):
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
