#The import function (tkinter) and what you want to type to call it back throughout your code (tk).
import tkinter as tk

#The class
class App():
    #In every class, you always need to have a def that starts with "__init__(self)"
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        #This tells the computer how big the window is.
        self.window.geometry("300x200")
        #This is the window title.
        self.window.title("My First GUI App")
        #This tells the computer to close the windows if I click on the close windows.
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)
        #This creates a label in the window that says "Hello" and the font is Arial and the size is 48.
        self.label = tk.Label(self.window, text="Hello", font=("Arial", 48))
        #This is the position that the label will be placed.
        self.label.place(x=20, y=20)

    def set_text(self, new_text):
        self.label.configure(text=new_text)

    def set_background(self, color):
        self.window.configure(bg=color)
        self.label.configure(bg=color)

    def set_foreground(self, color):
        self.label.configure(fg=color)

#These 2 lines tell tkinter to not run the default window but to run my own specifications for the window.
root = tk.Tk()
root.withdraw()

#This creates multiple windows if you want different windows.
window1 = App(root)
window2 = App(root)
window3 = App(root)

#This changes the label from "Hello" to whatever you specify in the brackets.
window2.set_text("Window 2")
window3.set_text("Window 3")

#This changes the background colour to whatever is specified.
window1.set_background("#800000")

#This changes the foreground colour to whatever is  specified.
window1.set_foreground("#ffffff")

#This just tells the computer to run this (root).
root.mainloop()