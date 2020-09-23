"""System Objects:
SystemApp,
SystemCanvas,
Frame
"""

from tkinter import Tk, Canvas, Frame


class SystemApp(Tk):
    """SystemApp - system app tk, inherits from tkinter.Tk.
    SystemApp Methods:

    """

    def __init__(self):
        super().__init__()
        self.space_canvas = SystemCanvas()
        self.space_frame = Frame()


class SystemCanvas(Canvas):
    """SystemCanvas - canvas of system app, inherits from tkinter.Canvas.
    SystemCanvas Methods:

    """

    def __init__(self):
        super().__init__()


class SystemFrame(Frame):
    """SystemFrame - frame of system app, inherits from tkinter.Frame.
    SystemFrame Methods:

    """
    def __init__(self):
        super().__init__()

