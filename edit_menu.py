from tkinter import *

def cut(text):
    text.event_generate("<<Cut>>")

def copy(text):
    text.event_generate("<<Copy>>")

def paste(text):
    text.event_generate("<<Paste>>")

def undo(text):
    text.edit_undo()

def redo(text):
    text.edit_redo()

def selectAll(text):
    text.tag_add(SEL, 1.0, END)
    text.mark_set(INSERT, 1.0)
    text.see(INSERT)

def main(root, text, menubar):
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=lambda: undo(text), accelerator="Ctrl+Z")
    editmenu.add_command(label="Redo", command=lambda: redo(text), accelerator="Ctrl+Y")
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=lambda: cut(text), accelerator="Ctrl+X")
    editmenu.add_command(label="Copy", command=lambda: copy(text), accelerator="Ctrl+C")
    editmenu.add_command(label="Paste", command=lambda: paste(text), accelerator="Ctrl+V")
    editmenu.add_separator()
    editmenu.add_command(label="Select All", command=lambda: selectAll(text), accelerator="Ctrl+A")
    menubar.add_cascade(label="Edit", menu=editmenu)

    root.bind('<Control-z>', lambda e: undo(text))
    root.bind('<Control-y>', lambda e: redo(text))
    root.bind('<Control-x>', lambda e: cut(text))
    root.bind('<Control-c>', lambda e: copy(text))
    root.bind('<Control-v>', lambda e: paste(text))
    root.bind('<Control-a>', lambda e: selectAll(text))
