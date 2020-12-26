import tkinter as tk

class Component:
    def set(self, property, value):
        self.component[property] = value

    def place(self, x, y, anchor="nw", **kwargs):
        """Place a widget in the parent widget. Use as options:
        in=master - master relative to which the widget is placed
        in_=master - see 'in' option description
        x=amount - locate anchor of this widget at position x of master
        y=amount - locate anchor of this widget at position y of master
        relx=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to width of master (1.0 is right edge)
        rely=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to height of master (1.0 is bottom edge)
        anchor=NSEW (or subset) - position anchor according to given direction
        width=amount - width of this widget in pixel
        height=amount - height of this widget in pixel
        relwidth=amount - width of this widget between 0.0 and 1.0
                          relative to width of master (1.0 is the same width
                          as the master)
        relheight=amount - height of this widget between 0.0 and 1.0
                           relative to height of master (1.0 is the same
                           height as the master)
        bordermode="inside" or "outside" - whether to take border width of
                                           master widget into account
        """
        self.component.place(x=x, y=y, anchor=anchor)

    def pack(self, **kwargs):
        """Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
        """
        self.component.pack(**kwargs)

class Indicator(Component):
    def __init__(self, window, text=None, **kwargs):
        """Construct a label widget with the parent MASTER.
        STANDARD OPTIONS
            activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground,
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, takefocus, text,
            textvariable, underline, wraplength
        WIDGET-SPECIFIC OPTIONS
            height, state, width
        """
        self.var = tk.StringVar(value=text)
        self.component = tk.Label(window, textvariable=self.var, **kwargs)

    def set_text(self, text):
        self.var.set(text)

class Button(Component):
    def __init__(self, window, **kwargs):
        """Construct a button widget with the parent MASTER.
        STANDARD OPTIONS
            activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, repeatdelay,
            repeatinterval, takefocus, text,
            textvariable, underline, wraplength
        WIDGET-SPECIFIC OPTIONS
            command, compound, default, height,
            overrelief, state, width
        """
        self.component = tk.Button(window, **kwargs)

class Entry(Component):
    def __init__(self, window, **kwargs):
        self.component = tk.Entry(window, **kwargs)

    def get(self):
        return self.component.get()

class Text(Component):
    def __init__(self, window, **kwargs):
        self.component = tk.Text(window, **kwargs)

    def get(self, index1=0.0, index2=None):
        return self.component.get(index1, index2)

    def insert(self, index=0.0):
        pass
    