tasks = []


def add_task():
	"""Ask for a task title and add it to the in-memory task list."""
	title = input("Enter task name: ").strip()

	if not title:
		print("Task name cannot be empty.")
		return

	task = {
		"title": title,
		"completed": False,
	}
	tasks.append(task)
	print("Task added successfully.")


def view_tasks():
	"""Display every task with its number and completion status."""
	if not tasks:
		print("No tasks found.")
		return

	print("\nYour Tasks:")
	for number, task in enumerate(tasks, start=1):
		status = "Done" if task["completed"] else "Pending"
		print(f"{number}. {task['title']} - {status}")


def complete_task():
	"""Mark a selected task as completed."""
	if not tasks:
		print("No tasks to complete.")
		return

	try:
		task_number = int(input("Enter task number to complete: "))
	except ValueError:
		print("Please enter a valid number.")
		return

	if task_number < 1 or task_number > len(tasks):
		print("Invalid task number.")
		return

	tasks[task_number - 1]["completed"] = True
	print("Task marked as completed.")


def delete_task():
	"""Delete a selected task from the list."""
	if not tasks:
		print("No tasks to delete.")
		return

	try:
		task_number = int(input("Enter task number to delete: "))
	except ValueError:
		print("Please enter a valid number.")
		return

	if task_number < 1 or task_number > len(tasks):
		print("Invalid task number.")
		return

	removed_task = tasks.pop(task_number - 1)
	print(f"Deleted: {removed_task['title']}")


def show_menu():
	"""Display the menu and return the user's choice."""
	print("\n==============================")
	print("          TO-DO LIST")
	print("==============================")
	print("1. Add Task")
	print("2. View Tasks")
	print("3. Complete Task")
	print("4. Delete Task")
	print("5. Exit")
	return input("\nEnter your choice: ").strip()


if __name__ == "__main__":
	while True:
		choice = show_menu()

		if choice == "1":
			add_task()
		elif choice == "2":
			view_tasks()
		elif choice == "3":
			complete_task()
		elif choice == "4":
			delete_task()
		elif choice == "5":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please select a number from 1 to 5.")
