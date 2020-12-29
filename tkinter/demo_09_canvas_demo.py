import tkinter as tk
from component import Indicator, Button, Message

class UserInterface:
    def __init__(self):
        self.window = self.build_window()

        self.canvas = tk.Canvas(self.window, height=200, width=200)
        self.canvas.place(x=200, y=0, anchor="n")
        x0, y0, x1, y1= 50, 50, 80, 80
        self.canvas.create_line(x0, y0, x1, y1)
        self.canvas.create_oval(x0, y0, x1, y1, fill='red')
        self.canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
        self.canvas.create_rectangle(100, 30, 100+20, 30+20)
        self.canvas.pack()

        self.quit_button = Button(self.window, text="Quit", width=10, height=2)
        self.quit_button.set("command", self.quit)
        self.quit_button.pack()
        self.quit_button.place(x=200, y=280, anchor="s")

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