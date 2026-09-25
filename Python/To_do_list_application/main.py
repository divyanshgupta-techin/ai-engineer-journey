"""Start the desktop To-Do application."""

import tkinter as tk

from ui import TodoApp


def main():
	root = tk.Tk()
	root.title("My To-Do List")
	root.geometry("800x600")
	root.minsize(560, 420)
	root.configure(bg=TodoApp.BACKGROUND)

	TodoApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()
