import tkinter as tk

class App():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry("300x200")
        self.window.title("My First GUI App")
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)
        self.label = tk.Label(self.window, text="What's your name?", font=("Arial", 18))
        self.label.place(x=20, y=20)

        #Add an entry box
        self.name_entry = tk.Entry(self.window)
        self.name_entry.insert(tk.END, "I am Groot")
        self.name_entry.place(x=20, y=100)
        self.name_entry.focus()

        #Add a button
        self.button = tk.Button(self.window, text="Click me!", command=self.do_something_exciting)
        self.button.place(x=20, y=150)
    
    def do_something_exciting(self):
        print("Clicked")
        self.window.configure(bg="#ff0000")
        self.label.configure(bg="#ff0000")
        name = self.name_entry.get()
        welcome = f"Hello, {name}. Welcome to my first GUI app!"
        self.label.configure(text=welcome)

root = tk.Tk()
root.withdraw()

window1 = App(root)

root.mainloop()