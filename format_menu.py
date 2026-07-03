from tkinter import *
from tkinter.font import Font

def bold(text):
    try:
        current_tags = text.tag_names("sel.first")
        if "bold" in current_tags:
            text.tag_remove("bold", "sel.first", "sel.last")
        else:
            text.tag_add("bold", "sel.first", "sel.last")
            bold_font = Font(text, text.cget("font"))
            bold_font.configure(weight="bold")
            text.tag_configure("bold", font=bold_font)
    except TclError:
        pass

def italic(text):
    try:
        current_tags = text.tag_names("sel.first")
        if "italic" in current_tags:
            text.tag_remove("italic", "sel.first", "sel.last")
        else:
            text.tag_add("italic", "sel.first", "sel.last")
            italic_font = Font(text, text.cget("font"))
            italic_font.configure(slant="italic")
            text.tag_configure("italic", font=italic_font)
    except TclError:
        pass

def underline(text):
    try:
        current_tags = text.tag_names("sel.first")
        if "underline" in current_tags:
            text.tag_remove("underline", "sel.first", "sel.last")
        else:
            text.tag_add("underline", "sel.first", "sel.last")
            underline_font = Font(text, text.cget("font"))
            underline_font.configure(underline=1)
            text.tag_configure("underline", font=underline_font)
    except TclError:
        pass

def changeColor(text, color):
    try:
        text.tag_add(color, "sel.first", "sel.last")
        text.tag_configure(color, foreground=color)
    except TclError:
        pass

def main(root, text, menubar):
    formatmenu = Menu(menubar, tearoff=0)

    formatmenu.add_command(label="Bold", command=lambda: bold(text), accelerator="Ctrl+B")
    formatmenu.add_command(label="Italic", command=lambda: italic(text), accelerator="Ctrl+I")
    formatmenu.add_command(label="Underline", command=lambda: underline(text), accelerator="Ctrl+U")
    formatmenu.add_separator()

    colormenu = Menu(formatmenu, tearoff=0)
    colormenu.add_command(label="Black", command=lambda: changeColor(text, "black"))
    colormenu.add_command(label="Red", command=lambda: changeColor(text, "red"))
    colormenu.add_command(label="Blue", command=lambda: changeColor(text, "blue"))
    colormenu.add_command(label="Green", command=lambda: changeColor(text, "green"))
    formatmenu.add_cascade(label="Text Color", menu=colormenu)

    menubar.add_cascade(label="Format", menu=formatmenu)

    root.bind('<Control-b>', lambda e: bold(text))
    root.bind('<Control-i>', lambda e: italic(text))
    root.bind('<Control-u>', lambda e: underline(text))
