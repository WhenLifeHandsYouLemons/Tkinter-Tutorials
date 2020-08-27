import tkinter as tk

class App():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry("300x200")
        self.window.title("My First GUI App")
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)
        self.label = tk.Label(self.window, text="Hello", font=("Arial", 64))
        self.label.place(x=20, y=20)
        #Add a button
        self.button = tk.Button(self.window, text="Click me!", command=self.do_something_exciting)
        self.button.place(x=20, y=120)
    
    def do_something_exciting(self):
        print("Clicked")
        self.window.configure(bg="#ff0000")
        self.label.configure(bg="#ff0000")
        self.label.configure(fg="#ffffff")        

root = tk.Tk()
root.withdraw()

window1 = App(root)

root.mainloop()