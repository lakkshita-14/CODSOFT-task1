import tkinter as tk
from tkinter import messagebox
class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("500x400")
        self.root.config(bg="lavender blush")  
        self.tasks = []

        self.task_entry = tk.Entry(root, width=30, font=('Consolas', 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task, font=('Consolas', 12), bg="pale violet red", fg="#ecf0f1")  
        add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=40, height=10, font=('Consolas', 12), bg="misty rose", fg="#2c3e50", selectbackground="thistle")  
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=('Consolas', 12), bg="light salmon", fg="#ecf0f1")  
        remove_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, font=('Consolas', 12), bg="plum", fg="#ecf0f1")  
        complete_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        update_button = tk.Button(root, text="Update Task", command=self.update_task, font=('Consolas', 12), bg="sky blue", fg="#2c3e50")  
        update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.task_listbox.bind('<Double-Button-1>', lambda event: self.update_task())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            completed_task = self.tasks.pop(selected_task_index[0])
            completed_task = f"[Done] {completed_task}"
            self.tasks.append(completed_task)
            self.update_task_list()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index[0]] = updated_task
                self.update_task_list()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()
