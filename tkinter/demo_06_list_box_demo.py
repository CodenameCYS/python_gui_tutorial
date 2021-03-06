import tkinter as tk
from component import Indicator, Button, Entry, Text, Listbox

class UserInterface:
    def __init__(self):
        self.window = self.build_window()

        self.panel = Indicator(self.window, font=("Arial", 12), width=30, height=3)
        self.panel.pack()
        self.panel.place(x=200, y=0, anchor="n")

        self.listbox = Listbox(self.window, ["A", "B", "C", "D"], height=4)
        self.listbox.pack()
        self.listbox.place(x=200, y=80, anchor="n")

        self.button = Button(self.window, text="Ok", width=10, height=1)
        self.button.set("command", self.click_button)
        self.button.pack()
        self.button.place(x=200, y=220, anchor="s")

        self.quit_button = Button(self.window, text="Quit", width=10, height=1)
        self.quit_button.set("command", self.quit)
        self.quit_button.pack()
        self.quit_button.place(x=200, y=260, anchor="s")

    def build_window(self):
        window = tk.Tk()
        window.title("user interface")
        window.geometry("400x300")
        return window

    def click_button(self):
        idx = self.listbox.component.curselection()
        selection = self.listbox.component.get(idx) if idx else "null"
        self.panel.set_text(f"your choice is {selection}")
        return

    def quit(self):
        self.window.quit()
        return

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()