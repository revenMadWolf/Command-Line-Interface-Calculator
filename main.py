
def show_tasks(task_list):
    for task_id, task, assignee, status in task_list:
        print(f"{task_id}: {task} — Assigned to {assignee} ({status})")

show_tasks(tasks)