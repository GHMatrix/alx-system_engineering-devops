#!/usr/bin/python3
"""
Python script that, using a REST API, retrieves and displays
information about an employee's TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <employee_id>".format(sys.argv[0]))

    employee_id = sys.argv[1]

    # Get user info
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_info.json()
    employee_name = user_data.get('name')

    # Get user's tasks
    user_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id))
    tasks_data = user_tasks.json()

    total_tasks = len(tasks_data)
    completed_tasks = [task for task in tasks_data if task.get('completed')]

    # Print the results as required
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task.get('title')))
