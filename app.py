from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg

import commandFunc
# retrive code for modules
from commandFunc import *

# define notebook object
class Notebook:
    def __init__(self, root):
        self.root = root
        self.root.title("Notebook Pro")
        self.root.geometry("700x500")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.wrapper()

    def wrapper(self):
        # place main frame center
        self.frame = Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.navBar = Frame(self.frame)
        self.navBar.grid(row=0, column=0, sticky="ew")

        # ================================
        # file menu
        # ================================
        self.fileBtn = ttk.Menubutton(self.navBar, text="File")
        self.fileMenu = Menu(self.fileBtn, tearoff=0)
        self.fileBtn["menu"] = self.fileMenu

        # adding each file option
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_command(label="Open")
        self.fileMenu.add_command(label="Save")
        self.fileMenu.add_command(label="Save As")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit")

        self.fileBtn.grid(row=0, column=0)


        # ================================
        # edit menu
        # ================================
        self.editBtn = ttk.Menubutton(self.navBar, text="Edit")
        self.editMenu = Menu(self.editBtn, tearoff=0)
        self.editBtn["menu"] = self.editMenu

        # add the edit items
        self.editMenu.add_command(label="Undo")
        self.editMenu.add_command(label="Redo")
        self.editMenu.add_command(label="Cut")
        self.editMenu.add_command(label="Copy")
        self.editMenu.add_command(label="Paste")
        self.editMenu.add_command(label="Select All")
        self.editMenu.add_command(label="Find")
        self.editMenu.add_command(label="Replace")
        self.editBtn.grid(row=0, column=1)

        # ================================
        # format menu
        # ================================
        self.formatBtn = ttk.Menubutton(self.navBar, text="Format")
        self.formatMenu = Menu(self.formatBtn, tearoff=0)
        self.formatBtn["menu"] = self.formatMenu

        # add format items
        self.formatMenu.add_command(label="Font")
        self.formatMenu.add_command(label="Word Wrap")
        self.formatMenu.add_command(label="Text Alignment")

        self.formatBtn.grid(row=0, column=2)

        # ================================
        # view menu
        # ================================
        self.viewBtn = ttk.Menubutton(self.navBar, text="View")
        self.viewMenu = Menu(self.viewBtn, tearoff=0)
        self.viewBtn["menu"] = self.viewMenu

        # adding view items
        self.viewMenu.add_command(label="Zoom")

        # add dark and light theme to the Theme label
        self.theme = Menu(self.viewMenu, tearoff=0)
        self.theme.add_radiobutton(label="Dark", command=lambda: commandFunc.darkTheme(self))
        self.theme.add_radiobutton(label="Light", command=lambda: commandFunc.lightTheme(self))
        self.viewMenu.add_cascade(label="Theme", menu=self.theme)

        self.viewMenu.add_command(label="Status Bar")

        self.viewBtn.grid(row=0, column=3)

        # ================================
        # tool menu
        # ================================
        self.toolBtn = ttk.Menubutton(self.navBar, text="Tools")
        self.toolMenu = Menu(self.toolBtn, tearoff=0)
        self.toolBtn["menu"] = self.toolMenu

        # adding tool items
        self.toolMenu.add_command(label="Word Count")
        self.toolMenu.add_command(label="Auto-save")

        self.toolBtn.grid(row=0, column=4)

        # text area
        self.textArea = Text(self.frame, padx=10, pady=10 ,font=("Verdana", 12), wrap="word")
        self.textArea.grid(row=1, column=0, sticky="nsew")


if __name__ == "__main__":
    root = Tk()
    app = Notebook(root)
    root.mainloop()