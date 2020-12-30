import tkinter as tk
import tkinter.messagebox
from component import Indicator, Button, Optionmenu

class UserInterface:
    def __init__(self):
        self.window = self.build_window()

        optionlist = ["showinfo", "showwarning", "showerror", "askyesno", "askretrycancel", "askquestion", "askokcancel"]
        self.optionmenu = Optionmenu(self.window, optionlist)
        self.optionmenu.pack()
        self.optionmenu.place(x=200, y=40, anchor="n")

        self.button = Button(self.window, text="Ok", width=10, height=2)
        self.button.set("command", self.click_button)
        self.button.pack()
        self.button.place(x=200, y=120, anchor="n")

        self.quit_button = Button(self.window, text="Quit", width=10, height=2)
        self.quit_button.set("command", self.quit)
        self.quit_button.pack()
        self.quit_button.place(x=200, y=200, anchor="n")

    def build_window(self):
        window = tk.Tk()
        window.title("user interface")
        window.geometry("400x300")
        return window

    def click_button(self):
        command = self.optionmenu.get()
        if command == "showinfo":
            tk.messagebox.showinfo(title="showinfo", message="show information")
        elif command == "showwarning":
            tk.messagebox.showwarning(title="showwarning", message="show warning")
        elif command == "showerror":
            tk.messagebox.showerror(title="showerror", message="show error")
        elif command == "askyesno":
            tk.messagebox.askyesno(title="askyesno", message="ask yes no")
        elif command == "askretrycancel":
            tk.messagebox.askretrycancel(title="askretrycancel", message="ask retry cancel")
        elif command == "askquestion":
            tk.messagebox.askquestion(title="askquestion", message="ask question")
        elif command == "askokcancel":
            tk.messagebox.askokcancel(title="askokcancel", message="ask ok cancel")
        return

    def quit(self):
        self.window.quit()
        return

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()