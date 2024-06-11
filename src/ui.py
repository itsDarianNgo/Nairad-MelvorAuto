# src/ui.py

from tkinter import Tk, Label


def create_ui():
    root = Tk()
    root.title("Melvor Idle Automation")
    Label(root, text="Melvor Idle Automation Script").pack()
    root.mainloop()


if __name__ == "__main__":
    create_ui()
