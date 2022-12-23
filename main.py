import tkinter as tk
from Forms import Forms


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Стрелецкая ЦРБ")
    root.geometry("280x140")
    app = Forms(root)
    app.createPanelWithButton()
    root.mainloop()

