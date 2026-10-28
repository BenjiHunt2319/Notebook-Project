from tkinter import *
from tkinter import TclError

# light and dark theme
def darkTheme(app):
    app.textArea.config(background="#333", foreground="#fff")
    app.navBar.config(background="#444")

def lightTheme(app):
    app.textArea.config(background="#fff", foreground="#111")
    app.navBar.config(background="#fff")
    

def toggle_style(self, style_name):
    try:
        # Check if text is actually selected
        if not self.textArea.tag_ranges("sel"):
            return
            
        # Get the current tags at the start of the selection
        current_tags = self.textArea.tag_names("sel.first")
            
        # Toggle the style tag on/off
        if style_name in current_tags:
            self.textArea.tag_remove(style_name, "sel.first", "sel.last")
        else:
            self.textArea.tag_add(style_name, "sel.first", "sel.last")
    except TclError:
        pass
