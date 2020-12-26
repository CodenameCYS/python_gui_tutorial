import tkinter as tk
from component import Indicator, Button, Entry, Text

class UserInterface:
    def __init__(self):
        self.window = self.build_window()

        self.panel = Indicator(self.window, font=("Arial", 12), width=30, height=3)
        self.panel.pack()
        self.panel.place(x=200, y=0, anchor="n")

        self.var0 = tk.StringVar(value="")
        self.radio_button_01 = tk.Radiobutton(self.window, text='Option A', variable=self.var0, value='A', command=self.update_text)
        self.radio_button_01.pack()
        self.radio_button_01.place(x=200, y=100, anchor="n")
        self.radio_button_02 = tk.Radiobutton(self.window, text='Option B', variable=self.var0, value='B', command=self.update_text)
        self.radio_button_02.pack()
        self.radio_button_02.place(x=200, y=150, anchor="n")

        self.var1 = tk.StringVar(value="")
        self.radio_button_03 = tk.Radiobutton(self.window, text='Option C', variable=self.var1, value='C', command=self.update_text)
        self.radio_button_03.pack()
        self.radio_button_03.place(x=200, y=200, anchor="n")
        self.var2 = tk.StringVar(value="")
        self.radio_button_04 = tk.Radiobutton(self.window, text='Option D', variable=self.var2, value='D', command=self.update_text)
        self.radio_button_04.pack()
        self.radio_button_04.place(x=200, y=250, anchor="n")

        self.panel.set_text(f"var0: {self.var0.get()}, var1: {self.var1.get()}, var2: {self.var2.get()}")

        self.quit_button = Button(self.window, text="Quit", width=10, height=2)
        self.quit_button.set("command", self.quit)
        self.quit_button.pack()
        self.quit_button.place(x=200, y=380, anchor="s")

    def build_window(self):
        window = tk.Tk()
        window.title("user interface")
        window.geometry("400x400")
        return window

    def update_text(self):
        self.panel.set_text(f"var0: {self.var0.get()}, var1: {self.var1.get()}, var2: {self.var2.get()}")
        return

    def quit(self):
        self.window.quit()
        return

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()