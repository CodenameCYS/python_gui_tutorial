import tkinter as tk
from component import Indicator, Button, Entry, Text

class UserInterface:
    def __init__(self):
        self.window = self.build_window()

        self.panel = Indicator(self.window, font=("Arial", 12), width=30, height=3)
        self.panel.pack()
        self.panel.place(x=200, y=0, anchor="n")

        self.var1 = tk.BooleanVar(value=False)
        self.check_button_01 = tk.Checkbutton(self.window, text='python', variable=self.var1, onvalue=True, offvalue=False, command=self.update_text)
        self.check_button_01.pack()
        self.check_button_01.place(x=200, y=100, anchor="n")
        
        self.var2 = tk.BooleanVar(value=False)
        self.check_button_02 = tk.Checkbutton(self.window, text='C++', variable=self.var2, onvalue=True, offvalue=False, command=self.update_text)
        self.check_button_02.pack()
        self.check_button_02.place(x=200, y=150, anchor="n")

        self.quit_button = Button(self.window, text="Quit", width=10, height=2)
        self.quit_button.set("command", self.quit)
        self.quit_button.pack()
        self.quit_button.place(x=200, y=280, anchor="s")

    def build_window(self):
        window = tk.Tk()
        window.title("user interface")
        window.geometry("400x300")
        return window

    def update_text(self):
        if self.var1.get() and self.var2.get():
            text = "both"
        elif self.var1.get():
            text = "python"
        elif self.var2.get():
            text = "C++"
        else:
            text = "Neither"
        self.panel.set_text(text)
        return

    def quit(self):
        self.window.quit()
        return

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()