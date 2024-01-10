#Creating GUI
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import DateEntry
from tkinter import ttk


#Date and Time
from datetime import datetime, timedelta

#Initialize the tasks list
tasks = []

#Import the new save file JSON
import json

#File that stores the task
#file_path = "Tasks.txt"

# Categories
categories = ["Personal", "Work", "Study", "Misc"]

# Selected category (default to "Other")
selected_category = None





#Functions for Adding, Viewing and Completing Saved Task
def add_task():
    global selected_category
    selected_category = tk.StringVar()
    selected_category.set("Misc")

    task = task_entry.get()
    due_date = get_due_date()
    category = selected_category.get()
    task_with_due_date = {
        "name": task,
        "due_date": due_date,
        "category": category
    }
    tasks.append(task_with_due_date)
    update_task_list()

    # Clear the entry fields after a successful task addition
    task_entry.delete(0, tk.END)
    due_date_entry.set_date(datetime.now())

def view_tasks():
    tasks_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks, start=1):
        tasks_listbox.insert(tk.END, f"{index}. {task['name']} (Due: {task['due_date']}, Category: {task['category']})")

def edit_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        old_task = tasks[index]

        # Prompt the user for the new task details
        new_task_name = simpledialog.askstring("Edit Task", f"Edit task name:\n\n{old_task['name']}\n\nNew task name:")
        new_due_date = simpledialog.askstring("Edit Task", f"Edit due date:\n\n{old_task['due_date']}\n\nNew due date:")
        new_category = simpledialog.askstring("Edit Task", f"Edit category:\n\n{old_task['category']}\n\nNew category:")

        if new_task_name:
            tasks[index]["name"] = new_task_name
            tasks[index]["due_date"] = new_due_date
            tasks[index]["category"] = new_category
            update_task_list()
    else:
        messagebox.showerror("Computer says no.", "Select a task.")

def update_task_list():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, f"{task['name']} (Due: {task['due_date']}, Category: {task['category']})")

def complete_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        completed_task = tasks.pop(index)
        update_task_list()
    else:
        messagebox.showerror("Computer says no.", "Select the task you wish to complete ;]")

def save_tasks_to_file():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        
def load_tasks_from_file():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def get_due_date():
    due_date_input = due_date_entry.get()
    if not due_date_input:
        return None
    try:
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
        return due_date.strftime("%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Computer says no.", "No can do! Please use YYYY-MM-DD :)")
        return None
    
def update_task_list():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, f"{task['name']} (Due: {task['due_date']}, Category: {task['category']})")

def on_closing():
    if messagebox.askokcancel("Computer says wait.", "Press Ok to save and if you think 9/11 was an inside job."):
        save_tasks_to_file()
        root.destroy()

def change_color_scheme():
    # Set background color of specific widgets
    for widget in [task_entry_label, due_date_entry_label, category_label, tasks_listbox_label]:
        widget.config(bg="lightblue", fg="black")

#Line bellow is old code for the first file save
#load_tasks_from_file()

# Load existing tasks from file on startup
tasks = load_tasks_from_file()








# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="white") #Sets the background colour
style = ttk.Style()
style.theme_use("clam") #Widgets

# Dropdown menu for task category
category_label = tk.Label(root, text="Select Category:")
category_label.pack(pady=5)
selected_category = tk.StringVar()
selected_category.set("Other")
category_menu = tk.OptionMenu(root, selected_category, *categories)
category_menu.pack(pady=5)

#Calendar Widget
due_date_label = tk.Label(root, text="Select Due Date:")
due_date_label.pack(pady=5)
due_date_entry = DateEntry(root, width=12, background="lightblue", foreground="black", borderwidth=2)
due_date_entry.pack(pady=5)

# Entry for task
task_entry_label = tk.Label(root, text="Enter Task:")
task_entry_label.pack(pady=5)
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# Entry for due date
due_date_entry_label = tk.Label(root, text="Enter Due Date (YYYY-MM-DD):")
due_date_entry_label.pack()
due_date_entry = tk.Entry(root)
due_date_entry.pack()

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, compound=tk.LEFT, padx=10)
add_button.pack(pady=10)

view_button = tk.Button(root, text="View Tasks", command=view_tasks, compound=tk.LEFT, padx=10)
view_button.pack(pady=10)

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack()

# Bind the Enter key to the Add Task button
root.bind("<Return>", lambda event=None: add_task())

# Listbox for tasks
tasks_listbox_label = tk.Label(root, text="Tasks:")
tasks_listbox_label.pack(pady=5)
tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=5, width=40, selectbackground="lightblue")
tasks_listbox.pack(pady=5)

scrollbar = tk.Scrollbar(root, command=tasks_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)

# Bind the on_closing function to the window close event
root.protocol("WM_DELETE_WINDOW", on_closing)







# Run the Tkinter event loop
root.mainloop()
