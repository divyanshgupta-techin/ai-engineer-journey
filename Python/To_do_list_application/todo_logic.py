"""Task storage and operations for the To-Do application."""

tasks = []


def add_task(title):
    """Add a pending task and return whether the title was valid."""
    cleaned_title = title.strip()

    if not cleaned_title:
        return False

    tasks.append({
        "title": cleaned_title,
        "completed": False,
    })
    return True


def get_tasks():
    """Return the current in-memory task list."""
    return tasks


def complete_task(task_index):
    """Toggle a task's completed state and return whether the index was valid."""
    if task_index < 0 or task_index >= len(tasks):
        return False

    tasks[task_index]["completed"] = not tasks[task_index]["completed"]
    return True


def delete_task(task_index):
    """Delete a task and return whether the index was valid."""
    if task_index < 0 or task_index >= len(tasks):
        return False

    tasks.pop(task_index)
    return True


def get_statistics():
    """Return total, pending, and completed task counts."""
    completed_count = sum(task["completed"] for task in tasks)
    total_count = len(tasks)

    return {
        "total": total_count,
        "completed": completed_count,
        "pending": total_count - completed_count,
    }