#!/usr/bin/python3
"""
Python script that, using a REST API, retrieves and displays
information about an employee's TODO list progress.
"""

import json
import requests
import sys


def fetch_employee_data(employee_id=None):
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

    return all_employee_data


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        employee_data = fetch_employee_data(employee_id)
    else:
        employee_data = fetch_employee_data()

    # Export data to JSON
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(employee_data, json_file, indent=4)
