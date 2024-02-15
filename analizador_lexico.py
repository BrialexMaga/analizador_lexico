import tkinter as tk
from alfabeto import Alfabeto

class AnalizadorLexico:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")
        self.root.geometry("800x405")



if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorLexico(root)
    root.mainloop()