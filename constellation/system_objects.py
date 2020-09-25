"""constellation Objects:
SystemApp,
SystemCanvas,
Frame
"""

from tkinter import Tk, Canvas, Frame, BOTH, YES


class SystemApp(Tk):
    """SystemApp - system app tk, inherits from tkinter.Tk.
    SystemApp Methods:

    """

    def __init__(self, window_width: int = 1200, window_height: int = 800, window_name: str = "Model", config_file_name: str = "input.txt"):
        super().__init__()
        self.space_canvas = SystemCanvas(self, window_width, window_height)
        self.space_frame = SystemFrame(self)
        self.geometry(f"{window_width}x{window_height}")
        self.title(window_name)

        self.initUI()

    def initUI(self):
        self.space_frame.initUI()
        self.space_canvas.initUI()

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass

    def input_config_from_file(self):
        pass


class SystemCanvas(Canvas):
    """SystemCanvas - canvas of system app, inherits from tkinter.Canvas.
    SystemCanvas Methods:

    """

    def __init__(self, app, window_width, window_height):
        super().__init__(
            app,
            width=window_width,
            height=window_height-200,
            bg='white'
        )
        self.w = window_width
        self.h = window_height - 200
        self.app = app

        app.bind('<Configure>', self.resize)

    def initUI(self):
        self.pack(side="bottom", expand=YES)
        self.place(y=200)

    def resize(self, event):
        self.w = event.width
        self.h = event.height

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass


class SystemFrame(Frame):
    """SystemFrame - frame of system app, inherits from tkinter.Frame.
    SystemFrame Methods:

    """

    def __init__(self, app):
        super().__init__()
        self.app = app

    def initUI(self):
        self.pack()

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass

    def input_config_from_file(self):
        pass
