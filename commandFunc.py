from tkinter import *

# light and dark theme
def darkTheme(app):
    app.textArea.config(background="#333", foreground="#fff")
    app.navBar.config(background="#444")

def lightTheme(app):
    app.textArea.config(background="#fff", foreground="#111")
    app.navBar.config(background="#fff")