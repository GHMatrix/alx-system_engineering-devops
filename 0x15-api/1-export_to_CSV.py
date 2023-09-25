#!/usr/bin/python3
"""
Python script that, using a REST API, retrieves and displays
information about an employee's TODO list progress and exports it to CSV.
"""

import csv
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

    # Prepare CSV file name based on USER_ID
    csv_file_name = '{}.csv'.format(user_id)

    # Create and write to the CSV file
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

        # Write task data to CSV with double quotes
        for task in tasks_data:
            writer.writerow(['"{}"'.format(user_id), '"{}"'
                            .format(username), '"{}"'.format(str(
                                task["completed"])), '"{}"'
                            .format(task["title"])])

    print("Data exported to {}".format(csv_file_name))
