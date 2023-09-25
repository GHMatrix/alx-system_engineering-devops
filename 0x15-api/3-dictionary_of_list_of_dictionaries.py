#!/usr/bin/python3
"""
Python script that, using a REST API, retrieves and displays
information about an employee's TODO list progress.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <employee_id>".format(sys.argv[0]))

    employee_id = sys.argv[1]
    all_employee_data = {}

    # Get all users
    users_info = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    users_data = users_info.json()

    for user in users_data:
        user_id = str(user['id'])
        username = user['username']

        # Get user's tasks
        user_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user_id))
        tasks_data = user_tasks.json()

        employee_tasks = []

        for task in tasks_data:
            task_dict = {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            employee_tasks.append(task_dict)

        all_employee_data[user_id] = employee_tasks

    # Export data to JSON
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employee_data, json_file, indent=4)
