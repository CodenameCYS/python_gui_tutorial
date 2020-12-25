import tkinter

def test():
    window = tkinter.Tk()
    for i in range(3):
        for j in range(3):
            if i == 1 and j >= 1:
                continue
            if (i+j) % 3 == 0:
                color = "red"
            elif (i+j) % 3 == 1:
                color = "yellow"
            else:
                color = "green"
            tkinter.Label(window, text="hello world!", bg=color).grid(row=i, column=j, padx=10, pady=10)
    tkinter.Label(window, text="hello world!", bg="blue").grid(row=0, column=0, padx=10, pady=10)
    tkinter.Label(window, text="hello world!", bg="red").grid(row=3, column=3, padx=10, pady=10)
    tkinter.Label(window, text="hello world!", bg="red").grid(row=5, column=3, padx=10, pady=10)
    # tkinter.Label(window, text="hello world!", bg="grey").grid(row=4, column=3, padx=20, pady=10)
    tkinter.Label(window, text="hello world!", bg="grey").grid(row=6, column=3, padx=10, pady=10)
    window.mainloop()

if __name__ == "__main__":
    test()