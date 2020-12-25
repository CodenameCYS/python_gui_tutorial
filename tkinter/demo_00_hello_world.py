import tkinter

class Window:
    def __init__(self):
        self.window = self.build_window()
        self.add_panel()
        # self.panel.place(x=100, y=30, anchor="nw")

    def build_window(self):
        window = tkinter.Tk() # 创建窗口实例
        window.title("user interface") # 设置窗口名称
        window.geometry("400x300") # 设置窗口大小
        return window

    def add_panel(self):
        self.panel = tkinter.Label(self.window, text="hello world!", bg="red", font=("Arial", 12), width=20, height=4) # 创建显示面板
        self.panel.pack() # 将显示面板放置到窗口当中

    def run(self):
        self.window.mainloop()
        return

if __name__ == "__main__":
    window = Window()
    window.run()
