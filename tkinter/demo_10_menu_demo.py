import tkinter as tk
from component import Indicator, Button, Entry, Text, Listbox, Optionmenu

class UserInterface:
    def __init__(self):
        self.window = self.build_window()

        self.panel = Indicator(self.window, font=("Arial", 12), width=30, height=3)
        self.panel.pack()
        self.panel.place(x=200, y=0, anchor="n")

        self.menu = tk.Menu(self.window)
        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="file", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="edit", menu=self.editmenu)
        self.submenu = tk.Menu(self.filemenu)
        self.filemenu.add_cascade(label="import", menu=self.submenu) 

        self.filemenu.add_command(label="New", command=self.do_job())
        self.filemenu.add_command(label="Open", command=self.do_job())
        self.filemenu.add_command(label="Save", command=self.do_job())
        self.filemenu.add_command(label="exit", command=self.quit)

        self.editmenu.add_command(label="cut", command=self.do_job())
        self.editmenu.add_command(label="copy", command=self.do_job())
        self.editmenu.add_command(label="paste", command=self.do_job())
        self.window.config(menu=self.menu)

        self.quit_button = Button(self.window, text="Quit", width=10, height=1)
        self.quit_button.set("command", self.quit)
        self.quit_button.pack()
        self.quit_button.place(x=200, y=260, anchor="s")

    def build_window(self):
        window = tk.Tk()
        window.title("user interface")
        window.geometry("400x300")
        return window

    def do_job(self):
        cnt = 0
        def fn():
            nonlocal cnt
            cnt += 1
            self.panel.set_text(f"op num: {cnt}")
            return
        return fn

    def quit(self):
        self.window.quit()
        return

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()