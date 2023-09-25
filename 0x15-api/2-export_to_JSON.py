#!/usr/bin/python3
"""
Python script that, using a REST API, retrieves and displays
information about an employee's TODO list progress and exports it to JSON.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <employee_id>".format(sys.argv[0]))

    employee_id = sys.argv[1]

    # Get user info
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    if user_info.status_code != 200:
        sys.exit("User not found")

    user_data = user_info.json()
    user_id = user_data.get('id')
    username = user_data.get('username')

    # Get user's tasks
    user_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id))
    if user_tasks.status_code != 200:
        sys.exit("User's tasks not found")

    tasks_data = user_tasks.json()

    # Prepare JSON data
    json_data = {str(user_id): [{"task": task["title"], "completed":
                                task["completed"], "username":
                                username} for task in tasks_data]}

    # Prepare JSON file name based on USER_ID
    json_file_name = '{}.json'.format(user_id)

    # Write JSON data to file
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Data exported to {}".format(json_file_name))
