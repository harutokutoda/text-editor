from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os

filename = None

def newFile(root, text):
    global filename
    filename = None
    root.title("Text Editor - Untitled")
    text.delete(1.0, END)

def openFile(root, text):
    global filename
    filename = askopenfilename(defaultextension=".txt", 
                               filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if filename:
        root.title(f"Text Editor - {os.path.basename(filename)}")
        text.delete(1.0, END)
        with open(filename, "r") as file:
            text.insert(1.0, file.read())

def saveFile(root, text):
    global filename
    if filename:
        with open(filename, "w") as file:
            file.write(text.get(1.0, END))
    else:
        saveAsFile(root, text)

def saveAsFile(root, text):
    global filename
    f = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                          filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if f:
        filename = f
        root.title(f"Text Editor - {os.path.basename(filename)}")
        with open(filename, "w") as file:
            file.write(text.get(1.0, END))

def exitEditor(root):
    if askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def main(root, text, menubar):
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=lambda: newFile(root, text), accelerator="Ctrl+N")
    filemenu.add_command(label="Open", command=lambda: openFile(root, text), accelerator="Ctrl+O")
    filemenu.add_command(label="Save", command=lambda: saveFile(root, text), accelerator="Ctrl+S")
    filemenu.add_command(label="Save As...", command=lambda: saveAsFile(root, text))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=lambda: exitEditor(root))
    menubar.add_cascade(label="File", menu=filemenu)

    root.bind('<Control-n>', lambda e: newFile(root, text))
    root.bind('<Control-o>', lambda e: openFile(root, text))
    root.bind('<Control-s>', lambda e: saveFile(root, text))
