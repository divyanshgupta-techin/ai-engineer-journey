"""Tkinter user interface for the To-Do application."""

import tkinter as tk
from tkinter import font, messagebox, ttk

import todo_logic


class TodoApp(tk.Frame):
    """Main window content and event handlers for the To-Do application."""

    PLACEHOLDER = "Enter a new task..."
    BACKGROUND = "#f5f7fb"
    CARD_BACKGROUND = "#ffffff"
    TEXT = "#1f2937"
    MUTED_TEXT = "#6b7280"
    ACCENT = "#2563eb"
    BORDER = "#e5e7eb"

    def __init__(self, master):
        super().__init__(master, bg=self.BACKGROUND)
        self.master = master
        self.task_rows = None
        self.canvas = None
        self.tasks_container = None
        self.task_entry = None
        self.total_value = tk.StringVar()
        self.pending_value = tk.StringVar()
        self.completed_value = tk.StringVar()

        self.configure_styles()
        self.create_widgets()
        self.refresh_tasks()

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Accent.TButton",
            background=self.ACCENT,
            foreground="white",
            borderwidth=0,
            padding=(16, 8),
            font=("Segoe UI", 10, "bold"),
        )
        style.map("Accent.TButton", background=[("active", "#1d4ed8")])
        style.configure(
            "Delete.TButton",
            background=self.CARD_BACKGROUND,
            foreground="#dc2626",
            borderwidth=1,
            padding=(10, 5),
            font=("Segoe UI", 9),
        )
        style.map("Delete.TButton", background=[("active", "#fef2f2")])
        style.configure(
            "App.Vertical.TScrollbar",
            background="#d1d5db",
            troughcolor=self.BACKGROUND,
            bordercolor=self.BACKGROUND,
            arrowcolor="#6b7280",
        )

    def create_widgets(self):
        self.pack(fill="both", expand=True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        header = tk.Frame(self, bg=self.BACKGROUND)
        header.grid(row=0, column=0, sticky="ew", padx=40, pady=(32, 20))

        tk.Label(
            header,
            text="My To-Do List",
            bg=self.BACKGROUND,
            fg=self.TEXT,
            font=("Segoe UI", 24, "bold"),
        ).pack(anchor="w")
        tk.Label(
            header,
            text="Stay organized. Get things done.",
            bg=self.BACKGROUND,
            fg=self.MUTED_TEXT,
            font=("Segoe UI", 11),
        ).pack(anchor="w", pady=(4, 0))

        add_area = tk.Frame(self, bg=self.BACKGROUND)
        add_area.grid(row=1, column=0, sticky="ew", padx=40, pady=(0, 18))
        add_area.columnconfigure(0, weight=1)

        self.task_entry = ttk.Entry(add_area, font=("Segoe UI", 11))
        self.task_entry.grid(row=0, column=0, sticky="ew", ipady=8, padx=(0, 10))
        self.task_entry.insert(0, self.PLACEHOLDER)
        self.task_entry.configure(foreground=self.MUTED_TEXT)
        self.task_entry.bind("<FocusIn>", self.clear_placeholder)
        self.task_entry.bind("<FocusOut>", self.restore_placeholder)
        self.task_entry.bind("<Return>", self.add_task_from_input)

        ttk.Button(
            add_area,
            text="Add Task",
            style="Accent.TButton",
            command=self.add_task_from_input,
        ).grid(row=0, column=1)

        tk.Label(
            self,
            text="Tasks",
            bg=self.BACKGROUND,
            fg=self.TEXT,
            font=("Segoe UI", 14, "bold"),
        ).grid(row=2, column=0, sticky="w", padx=40, pady=(0, 10))

        list_area = tk.Frame(self, bg=self.BACKGROUND)
        list_area.grid(row=3, column=0, sticky="nsew", padx=40)
        list_area.columnconfigure(0, weight=1)
        list_area.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            list_area,
            bg=self.BACKGROUND,
            highlightthickness=0,
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            list_area,
            orient="vertical",
            command=self.canvas.yview,
            style="App.Vertical.TScrollbar",
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.tasks_container = tk.Frame(self.canvas, bg=self.BACKGROUND)
        self.task_rows = self.canvas.create_window(
            (0, 0),
            window=self.tasks_container,
            anchor="nw",
        )
        self.tasks_container.bind(
            "<Configure>",
            lambda event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )
        self.canvas.bind(
            "<Configure>",
            lambda event: self.canvas.itemconfigure(
                self.task_rows,
                width=event.width,
            ),
        )
        self.canvas.bind("<Enter>", self.enable_mousewheel)
        self.canvas.bind("<Leave>", self.disable_mousewheel)

        statistics = tk.Frame(self, bg=self.CARD_BACKGROUND)
        statistics.grid(row=4, column=0, sticky="ew", padx=40, pady=(20, 32))
        statistics.columnconfigure((0, 1, 2), weight=1)
        self.create_statistic(statistics, 0, "Total Tasks", self.total_value)
        self.create_statistic(statistics, 1, "Pending Tasks", self.pending_value)
        self.create_statistic(
            statistics,
            2,
            "Completed Tasks",
            self.completed_value,
        )

    def create_statistic(self, parent, column, label_text, value_variable):
        statistic = tk.Frame(parent, bg=self.CARD_BACKGROUND)
        statistic.grid(row=0, column=column, padx=20, pady=14)
        tk.Label(
            statistic,
            textvariable=value_variable,
            bg=self.CARD_BACKGROUND,
            fg=self.TEXT,
            font=("Segoe UI", 18, "bold"),
        ).pack()
        tk.Label(
            statistic,
            text=label_text,
            bg=self.CARD_BACKGROUND,
            fg=self.MUTED_TEXT,
            font=("Segoe UI", 9),
        ).pack(pady=(2, 0))

    def clear_placeholder(self, _event=None):
        if self.task_entry.get() == self.PLACEHOLDER:
            self.task_entry.delete(0, tk.END)
            self.task_entry.configure(foreground=self.TEXT)

    def restore_placeholder(self, _event=None):
        if not self.task_entry.get().strip():
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, self.PLACEHOLDER)
            self.task_entry.configure(foreground=self.MUTED_TEXT)

    def add_task_from_input(self, _event=None):
        title = self.task_entry.get()
        if title == self.PLACEHOLDER:
            title = ""

        if not todo_logic.add_task(title):
            messagebox.showwarning(
                "Empty task",
                "Please enter a task before adding it.",
            )
            return "break"

        self.task_entry.delete(0, tk.END)
        self.task_entry.configure(foreground=self.TEXT)
        self.refresh_tasks()
        self.task_entry.focus_set()
        return "break"

    def enable_mousewheel(self, _event=None):
        self.canvas.bind_all("<MouseWheel>", self.scroll_tasks)

    def disable_mousewheel(self, _event=None):
        self.canvas.unbind_all("<MouseWheel>")

    def scroll_tasks(self, event):
        scroll_units = int(-event.delta / 120) or (-1 if event.delta < 0 else 1)
        self.canvas.yview_scroll(scroll_units, "units")

    def refresh_tasks(self):
        for child in self.tasks_container.winfo_children():
            child.destroy()

        tasks = todo_logic.get_tasks()

        if not tasks:
            tk.Label(
                self.tasks_container,
                text="No tasks yet.\nAdd your first task to get started.",
                bg=self.BACKGROUND,
                fg=self.MUTED_TEXT,
                font=("Segoe UI", 11),
                justify="center",
                pady=50,
            ).pack(fill="x")
        else:
            for task_index, task in enumerate(tasks):
                self.create_task_row(task_index, task)

        self.refresh_statistics()

    def create_task_row(self, task_index, task):
        row = tk.Frame(
            self.tasks_container,
            bg=self.CARD_BACKGROUND,
            highlightbackground=self.BORDER,
            highlightthickness=1,
        )
        row.pack(fill="x", pady=(0, 8))
        row.columnconfigure(1, weight=1)

        completed = tk.BooleanVar(value=task["completed"])
        tk.Checkbutton(
            row,
            variable=completed,
            command=lambda: self.toggle_task(task_index),
            bg=self.CARD_BACKGROUND,
            activebackground=self.CARD_BACKGROUND,
            selectcolor=self.CARD_BACKGROUND,
            cursor="hand2",
        ).grid(row=0, column=0, padx=(12, 4), pady=12)

        task_font = font.Font(
            family="Segoe UI",
            size=10,
            overstrike=task["completed"],
        )
        tk.Label(
            row,
            text=task["title"],
            bg=self.CARD_BACKGROUND,
            fg=self.MUTED_TEXT if task["completed"] else self.TEXT,
            font=task_font,
            anchor="w",
        ).grid(row=0, column=1, sticky="ew", pady=12)

        ttk.Button(
            row,
            text="Delete",
            style="Delete.TButton",
            command=lambda: self.delete_task(task_index),
        ).grid(row=0, column=2, padx=12, pady=8)

    def toggle_task(self, task_index):
        if todo_logic.complete_task(task_index):
            self.refresh_tasks()

    def delete_task(self, task_index):
        tasks = todo_logic.get_tasks()
        if task_index < 0 or task_index >= len(tasks):
            return

        should_delete = messagebox.askyesno(
            "Delete task",
            f"Delete '{tasks[task_index]['title']}'?",
        )
        if should_delete and todo_logic.delete_task(task_index):
            self.refresh_tasks()

    def refresh_statistics(self):
        statistics = todo_logic.get_statistics()
        self.total_value.set(str(statistics["total"]))
        self.pending_value.set(str(statistics["pending"]))
        self.completed_value.set(str(statistics["completed"]))