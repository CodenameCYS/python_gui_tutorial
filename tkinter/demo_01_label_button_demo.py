import tkinter as tk

class Button:
    def __init__(self, window, text="Ok", width=10, height=2):
        self.button = tk.Button(window, text=text, width=width, height=height)
        self.button.pack()

    def set_click_motion(self, fn):
        self.button["command"] = fn

    def set_place(self, x, y, anchor="nw"):
        self.button.place(x=x, y=y, anchor=anchor)

class Panel:
    def __init__(self, window):
        self.var = tk.StringVar()
        self.panel = tk.Label(window, textvariable=self.var, bg="red", font=("Arial", 12), width=15, height=3)
        self.panel.pack()

    def set_text(self, text):
        self.var.set(text)

    def set_bg_color(self, color):
        self.panel["bg"] = color

    def set_place(self, x, y, anchor="nw"):
        self.panel.place(x=x, y=y, anchor=anchor)

class UserInterface:
    def __init__(self):
        self.window = self.build_window()
        self.panel = Panel(self.window)
        self.button = Button(self.window)
        self.button.set_click_motion(self.click_button())

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
                self.panel.set_bg_color("green")
            else:
                self.panel.set_text("")
                self.panel.set_bg_color("red")
            status = not status
            return
        return fn

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()