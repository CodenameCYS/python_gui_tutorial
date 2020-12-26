import tkinter as tk
from component import Indicator, Button

class UserInterface:
    def __init__(self):
        self.window = self.build_window()

        self.panel = Indicator(self.window, bg="red", font=("Arial", 12), width=30, height=3)
        self.panel.pack()
        self.panel.place(x=200, y=80, anchor="n")
        
        self.button = Button(self.window, text="Ok", width=10, height=2)
        self.button.set("command", self.click_button())
        self.button.pack()
        self.button.place(x=20, y=280, anchor="sw")

        self.quit_button = Button(self.window, text="Quit", width=10, height=2)
        self.quit_button.set("command", self.quit)
        self.quit_button.pack()
        self.quit_button.place(x=380, y=280, anchor="se")

    def build_window(self):
        window = tk.Tk()
        window.title("user interface")
        window.geometry("400x300")
        return window

    def click_button(self):
        status = False
        def fn():
            nonlocal status
            if not status:
                self.panel.set_text("hello world!")
                self.panel.set("bg", "green")
            else:
                self.panel.set_text("")
                self.panel.set("bg", "red")
            status = not status
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